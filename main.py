from groq import Groq

import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.getenv('GROQ_API_KEY_1'),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": """
            Escreva um texto em português do Brasil, sobre:
            A importância das IAs na criação de conteúdos para Posts e Redes Sociais.
            """,
        }
    ],
    model="llama3-8b-8192",
    stream=False,
)

print(chat_completion.choices[0].message.content)