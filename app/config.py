from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    GOOGLE_API_KEY: str

    UPLOAD_FOLDER: str = "uploads"

    VECTOR_DB: str = "vector_db"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    LLM_MODEL: str = "gemini-2.5-flash"

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    TOP_K: int = 5

    TEMPERATURE: float = 0.2

    MAX_OUTPUT_TOKENS: int = 1024

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()