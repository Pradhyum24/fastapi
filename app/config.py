
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
load_dotenv() # Call load_dotenv() at the top of the file

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # This tells Pydantic to look for .env file in the current working directory
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()