from pathlib import Path
from typing import List

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


class HealthcareVectorStore:
    def __init__(self, db_dir: str, collection_name: str = "healthcare_docs") -> None:
        Path(db_dir).mkdir(parents=True, exist_ok=True)
        self.client = chromadb.PersistentClient(path=db_dir)
        self.embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn,
        )

    def add_documents(self, docs: List[str]) -> None:
        ids = [f"doc_{idx}" for idx in range(len(docs))]
        self.collection.upsert(documents=docs, ids=ids)

    def query(self, query_text: str, top_k: int = 4) -> List[str]:
        result = self.collection.query(query_texts=[query_text], n_results=top_k)
        return result.get("documents", [[]])[0]
