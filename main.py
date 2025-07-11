from dotenv import load_dotenv
from langchain_groq import ChatGroq
from agents.linkedin_lookup import ReAct_agent
from config import Config


load_dotenv()


llm = ChatGroq(
    model=Config.model,
    temperature=0.0
)

if __name__ == "__main__":
    print(ReAct_agent(llm))
