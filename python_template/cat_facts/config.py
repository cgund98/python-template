from pydantic_settings import BaseSettings


class Config(BaseSettings):
    cats_api_base: str = "https://catfact.ninja"


config = Config()
