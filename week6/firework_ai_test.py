import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(override=True)


from fireworks import Fireworks

client = Fireworks()

response = client.chat.completions.create(
  model="accounts/fireworks/models/deepseek-v4p1-flash",
  messages=[{
    "role": "user",
    "content": "Say hello in Spanish",
  }],
)

print(response.choices[0].message.content)