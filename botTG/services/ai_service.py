import openai
from config import OPENAI_API_KEY

# Инициализация клиента OpenAI
client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

async def ask_gpt(prompt: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",  # или модель, которую ты используешь
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content