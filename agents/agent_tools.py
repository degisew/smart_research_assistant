from langchain.tools import tool
from langchain_tavily import TavilySearch


@tool
def search_tool(query: str):
    """
    Search a user linkedin profile by the given name.
    """
    search = TavilySearch()
    res = search.run(query)
    return res
