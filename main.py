from dotenv import load_dotenv
from langchain_groq import ChatGroq
from agents.linkedin_lookup import get_user_summary
from agents.linkedin_lookup import ReAct_agent
from config import Config


load_dotenv()


llm = ChatGroq(
    model=Config.model,
    temperature=0.0
)

if __name__ == "__main__":
    lnkdn_url = ReAct_agent(llm)
    print(get_user_summary(llm, lnkdn_url))
