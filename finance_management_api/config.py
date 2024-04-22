import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
