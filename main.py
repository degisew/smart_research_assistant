from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import Config
from data.linkedin_scrap import get_linkedin_user_profile

load_dotenv()


summary_template = """
Given the linkedin information {info} about the person from, I want you to create:
1. a short summary
2. two interesting facts about them
"""
summary_prompt_template = PromptTemplate(
    input_variables=["info"], template=summary_template)


llm = ChatGroq(
    model=Config.model,
    temperature=0.0,
)
info = get_linkedin_user_profile(Config.gist_url)

chain = summary_prompt_template | llm | StrOutputParser()

res = chain.invoke(input={"info": info})

print(res)
