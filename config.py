import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    model = os.environ["MODEL"]
    gist_url = os.environ["GIST_URL"]
