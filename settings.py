import os
from dotenv import load_dotenv
load_dotenv()

YATR_KEY = os.getenv("YATR_KEY")
AIRTABLE_KEY = os.getenv("AIRTABLE_KEY")