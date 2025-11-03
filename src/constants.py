import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
USERNAME = os.getenv("USERNAME")
DOMAIN = "x.com"
COOKIES_FILE = "cookies.json"
