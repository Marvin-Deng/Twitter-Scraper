import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
DOMAIN = "x.com"
COOKIES_FILE = "cookies.json"
