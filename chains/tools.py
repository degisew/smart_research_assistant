from langchain_core.tools import tool
from langchain_tavily import TavilySearch


@tool
def search_company(company_name: str):
    """Web search for public info about a company."""

    engine = TavilySearch()

    return engine.run(company_name)
