import requests
from langchain.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from config import Config


def get_linkedin_user_profile():
    url = Config.gist_url
    res = requests.get(url)

    return res.json()


def get_user_summary(llm):
    summary_template = """
    Given the linkedin information {info} about the person from, I want you to create:
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["info"], template=summary_template)

    info = get_linkedin_user_profile()

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"info": info})

    return res
