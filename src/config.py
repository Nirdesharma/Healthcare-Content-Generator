from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class AppConfig:
    groq_api_key: str
    groq_base_url: str
    groq_model: str
    vector_db_dir: str
    top_k_context: int

    @classmethod
    def from_env(cls) -> "AppConfig":
        load_dotenv()

        api_key = os.getenv("GROQ_API_KEY", "").strip()
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing. Set it in .env file.")

        return cls(
            groq_api_key=api_key,
            groq_base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
            groq_model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            vector_db_dir=os.getenv("VECTOR_DB_DIR", "./vector_db"),
            top_k_context=int(os.getenv("TOP_K_CONTEXT", "4")),
        )
