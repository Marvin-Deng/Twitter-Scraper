import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")
DOMAIN = "x.com"
COOKIES_FILE = "cookies.json"
