from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

from .agent_tools import search_tool


def ReAct_agent(llm):
    full_name = "Degisew Mengist Python Developer"

    template = """
    Given the person full name {full_name}, I want you to give me the linkedin url.
    Please Note that your answer should only contain the URL.
    """

    prompt_template = PromptTemplate(
        input_variables=["full_name"], template=template)

    tools = [search_tool]

    react_prompt = hub.pull("hwchase17/react")

    react_agent = create_react_agent(llm, tools=tools, prompt=react_prompt)

    executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True)

    res = executor.invoke(
        {"input": prompt_template.format_prompt(full_name=full_name)})

    return res["output"]


def get_user_summary(llm, lnkdn_url):
    summary_template = """
    Given the linkedin information {info} about the person from, I want you to create:
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template)

    # info = get_linkedin_user_profile()

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"info": lnkdn_url})

    return res
