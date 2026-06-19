from openai import OpenAI

from src.utils import get_env


client = OpenAI(
    api_key=get_env("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def summarize(text):

    if not text or len(text.strip()) < 50:
        print("Skipping empty transcript")
        return None

    prompt = f"""
Summarize:

{text[:15000]}

Return:

Main ideas
Concepts
Examples
"""

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return r.choices[0].message.content