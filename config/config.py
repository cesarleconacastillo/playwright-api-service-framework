import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BASE_URL = os.getenv("BASE_URL")

    AUTH_USER = os.getenv("AUTH_USER")

    AUTH_PWD = os.getenv("AUTH_PWD")