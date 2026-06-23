import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PORT: int = int(os.getenv('PORT', 8000))
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    JWT_ACCESS_SECRET: str = os.getenv('JWT_ACCESS_SECRET')
    JWT_REFRESH_SECRET: str = os.getenv('JWT_REFRESH_SECRET')

settings = Settings()