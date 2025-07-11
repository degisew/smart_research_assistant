import requests


def get_linkedin_user_profile(url: str):
    res = requests.get(url)
    return res.json()
