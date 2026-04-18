import streamlit as st

from src.config import AppConfig
from src.generator import HealthcareContentGenerator

st.set_page_config(page_title="Healthcare Content Generator", layout="wide")


def init_generator() -> HealthcareContentGenerator:
    config = AppConfig.from_env()
    return HealthcareContentGenerator(config=config)


def main() -> None:
    st.title("Healthcare Content Generator")
    st.caption("GenAI assistant for structured healthcare documentation")

    with st.sidebar:
        st.header("Generation Settings")
        output_type = st.selectbox(
            "Output Type",
            ["Patient Summary", "Clinical Note", "Discharge Instructions"],
            index=0,
        )
        audience = st.selectbox(
            "Audience",
            ["Healthcare Professional", "Patient Friendly", "Caregiver"],
            index=0,
        )
        tone = st.selectbox(
            "Tone",
            ["Professional", "Empathetic", "Concise", "Educational"],
            index=0,
        )

    topic = st.text_area(
        "Enter Topic or Clinical Scenario",
        placeholder="Example: 58-year-old patient with type 2 diabetes, elevated HbA1c, and recent lifestyle changes.",
        height=150,
    )

    if st.button("Generate Content", type="primary"):
        if not topic.strip():
            st.warning("Please provide a topic or scenario first.")
            return

        with st.spinner("Generating healthcare content..."):
            try:
                generator = init_generator()
                result = generator.generate(
                    topic=topic,
                    output_type=output_type,
                    audience=audience,
                    tone=tone,
                )
            except Exception as exc:
                st.error(f"Generation failed: {exc}")
                return

        st.subheader("Generated Output")
        st.markdown(result["content"])

        with st.expander("Retrieved Knowledge Context"):
            for idx, ctx in enumerate(result["context"], start=1):
                st.markdown(f"**Context {idx}:** {ctx}")


if __name__ == "__main__":
    main()
