import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name = os.environ["APP_NAME"]
    openrouter_api_key=os.environ["OPENROUTER_API_KEY"]


settings = Settings()
