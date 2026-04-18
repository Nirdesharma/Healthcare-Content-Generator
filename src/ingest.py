from pathlib import Path

from src.config import AppConfig
from src.vector_store import HealthcareVectorStore


def chunk_text(text: str, chunk_size: int = 120) -> list[str]:
    text = text.strip()
    if not text:
        return []

    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if len(current) >= chunk_size:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks


def ingest_knowledge_base() -> None:
    config = AppConfig.from_env()
    vector_store = HealthcareVectorStore(db_dir=config.vector_db_dir)

    kb_path = Path("data/healthcare_knowledge_base.txt")
    if not kb_path.exists():
        raise FileNotFoundError(f"Knowledge base file not found: {kb_path}")

    raw_text = kb_path.read_text(encoding="utf-8")
    documents = chunk_text(raw_text, chunk_size=120)

    if not documents:
        raise ValueError("Knowledge base is empty after chunking.")

    vector_store.add_documents(documents)
    print(f"Ingested {len(documents)} chunks into vector database.")


if __name__ == "__main__":
    ingest_knowledge_base()
