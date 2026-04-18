SYSTEM_PROMPT = """
You are a senior healthcare documentation specialist.

Rules:
1. Use medically accurate, professional terminology.
2. Keep output clear, consistent, and properly structured.
3. Do not invent patient-specific facts not provided by the user/context.
4. If details are missing, use neutral placeholders and mention assumptions.
5. Keep tone aligned with requested audience and style.
6. Include a brief safety statement where appropriate.
"""


def build_user_prompt(topic: str, output_type: str, audience: str, tone: str, context_blocks: list[str]) -> str:
    context_text = "\n\n".join([f"- {block}" for block in context_blocks]) or "- No retrieved context available."

    return f"""
Task: Generate a high-quality healthcare {output_type}.

Input Topic/Scenario:
{topic}

Target Audience: {audience}
Preferred Tone: {tone}

Retrieved Domain Context:
{context_text}

Output Requirements:
- Start with a short title.
- Use structured section headers.
- Keep language precise and professional.
- Include standard healthcare phrasing where suitable.
- Add a brief disclaimer: 'For clinical review only.'
"""
