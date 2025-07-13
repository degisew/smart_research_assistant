import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    model = os.environ["MODEL"]
