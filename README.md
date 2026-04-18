# Healthcare Content Generator

A specialized GenAI content generation project for healthcare professionals.
This app converts simple topic inputs into structured, professional healthcare documents such as patient summaries.

## Features

- Prompt-engineered output templates for clinical writing
- Retrieval-augmented generation using a vector database (ChromaDB)
- Groq Llama integration using OpenAI-compatible API format
- Streamlit frontend for interactive usage
- Built-in sample healthcare knowledge base for grounding outputs

## Tech Stack

- Python 3.10+
- Streamlit (frontend)
- ChromaDB (vector database)
- SentenceTransformers (embedding model)
- Groq Llama API (LLM API)

## Project Structure

```text
Healthcare-Content-Generator/
|- app.py
|- requirements.txt
|- .env.example
|- README.md
|- data/
|  |- healthcare_knowledge_base.txt
|- src/
|  |- config.py
|  |- prompts.py
|  |- vector_store.py
|  |- llm_client.py
|  |- generator.py
|  |- ingest.py
```

## Setup in VS Code

1. Open folder in VS Code: File -> Open Folder -> D:\Healthcare-Content-Generator
2. Open terminal in VS Code.
3. Create and activate virtual environment:
   - python -m venv .venv
   - .venv\Scripts\Activate.ps1
4. Install dependencies:
   - pip install -r requirements.txt
5. Configure environment:
   - copy .env.example .env
   - Edit .env and set GROQ_API_KEY=your_key_here
6. Build vector database:
   - python -m src.ingest
7. Run Streamlit app:
   - streamlit run app.py


