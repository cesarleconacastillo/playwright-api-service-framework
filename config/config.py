import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("AUTH_USER")

    PASSWORD = os.getenv("AUTH_PWD")