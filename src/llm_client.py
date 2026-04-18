from openai import OpenAI


class LLMClient:
    def __init__(self, api_key: str, base_url: str, model: str) -> None:
        # Groq exposes an OpenAI-compatible chat completion endpoint.
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content or "No content generated."
