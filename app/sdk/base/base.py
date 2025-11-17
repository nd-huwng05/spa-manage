from dotenv import load_dotenv
import os

def load_env():
    if not load_dotenv(os.path.expanduser("/config/.env")):
        if not load_dotenv(os.path.expanduser(".env")):
            return Exception("Can't find .env file")
    return None