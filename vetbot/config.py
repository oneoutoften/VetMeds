import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()

@dataclass
class Config:
    TOKEN: str = os.getenv("BOT_TOKEN", "")
    DB_URL: str = os.getenv(
        "DB_URL", 
        "postgresql+asyncpg://vet_user:vetpass123@postgres:5432/vet_drugs_db"
    )

config = Config()