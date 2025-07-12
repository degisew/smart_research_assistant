from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain_groq import ChatGroq

from config import Config

from .agent_tools import search_tool
from .output_parsers import Parser, summary_parser


def ReAct_agent(llm, user_name):
    # user_name = "Degisew Mengist Python Developer"

    template = """
    Given the person full name {user_name}, I want you to give me the linkedin url.
    Please Note that your answer should only contain the URL.
    """

    prompt_template = PromptTemplate(
        input_variables=["user_name"], template=template)

    tools = [search_tool]

    react_prompt = hub.pull("hwchase17/react")

    react_agent = create_react_agent(llm, tools=tools, prompt=react_prompt)

    executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True)

    res = executor.invoke(
        {"input": prompt_template.format_prompt(user_name=user_name)})

    return res["output"]


def get_user_summary(user_name) -> Parser:
    llm = ChatGroq(
        model=Config.model,
        temperature=0.0
    )

    lnkdn_url = ReAct_agent(llm, user_name)

    summary_template = """
    Given the linkedin information {info} about the person from, I want you to create:
    1. a short summary
    2. two interesting facts about them
    \n {format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["info"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()}
    )

    # info = get_linkedin_user_profile()

    chain = summary_prompt_template | llm | summary_parser

    res = chain.invoke(input={"info": lnkdn_url})

    return res
