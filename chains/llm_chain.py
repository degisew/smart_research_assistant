from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from chains.output_parsers import OutputParser, summary_parser
from config import Config

from chains.tools import search_company


def generate_company_summary(company_name: str) -> OutputParser:
    llm = ChatGroq(
        model=Config.model,
        temperature=0.0
    )

    template = """
    Given the startup company name, {company_name}, provide:
    1. A brief company summary
    2. Background on the team
    3. Top 5 biggest competitors in country wide or continent(if it's big).
    4. 3 smart questions to ask a founder

    {format_instructions}
    """

    prompt_template = PromptTemplate(
        input_variables=["company_name"],
        template=template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()}
    )

    tools = [search_company]

    react_prompt = hub.pull("hwchase17/react")

    react_agent = create_react_agent(llm, tools, react_prompt)

    agent_executor = AgentExecutor(
        agent=react_agent, tools=tools, verbose=True)

    prompt_text = prompt_template.format_prompt(
        company_name=company_name)

    raw_result = agent_executor.invoke({"input": prompt_text})

    parsed_data = summary_parser.parse(raw_result["output"])

    return parsed_data
