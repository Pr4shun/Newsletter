import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


NEWS_API_KEY = os.getenv("NEWS_API_KEY")


print(NEWS_API_KEY)
