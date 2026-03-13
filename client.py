import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getend("API_KEY")
if not api_key:
    raise ValueError("Missing API_KEY")