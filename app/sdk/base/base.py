from dotenv import load_dotenv
import os

def load_env():
    if not load_dotenv(os.path.expanduser(".env")):
        if not load_dotenv(os.path.expanduser("../.env")):
            return Exception("Can't find .env file")
    return None