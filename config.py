from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FILE_NAME: str
    PAGE_SIZE: int
    SORT_BY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
