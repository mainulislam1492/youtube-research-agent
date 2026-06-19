import os
from dotenv import load_dotenv

load_dotenv()


def get_env(name):
    value = os.getenv(name)

    if not value:
        raise Exception(f"{name} missing")

    return value