from groq import Groq
from prompts import TECH_PROMPT

client = Groq()  # Uses GROQ_API_KEY from environment variable

def ask_tech_questions(tech_stack):
    prompt = TECH_PROMPT.format(tech_stack=tech_stack)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
