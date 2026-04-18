from src.config import AppConfig
from src.llm_client import LLMClient
from src.prompts import SYSTEM_PROMPT, build_user_prompt
from src.vector_store import HealthcareVectorStore


class HealthcareContentGenerator:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.vector_store = HealthcareVectorStore(db_dir=config.vector_db_dir)
        self.llm = LLMClient(
            api_key=config.groq_api_key,
            base_url=config.groq_base_url,
            model=config.groq_model,
        )

    def generate(self, topic: str, output_type: str, audience: str, tone: str) -> dict:
        context_blocks = self.vector_store.query(query_text=topic, top_k=self.config.top_k_context)

        user_prompt = build_user_prompt(
            topic=topic,
            output_type=output_type,
            audience=audience,
            tone=tone,
            context_blocks=context_blocks,
        )

        generated_content = self.llm.generate(system_prompt=SYSTEM_PROMPT, user_prompt=user_prompt)

        return {"content": generated_content, "context": context_blocks}
