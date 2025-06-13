import os
from openai import OpenAI

# Nếu các bạn dùng GroqAI
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='',
)

while 1 == 1:
    print("Enter your message: ")
    userInput = input()
    if userInput == "exit":
        break
    else:
        stream = client.chat.completions.create(
            messages = [
                {
                    "role": "user",
                    "content": userInput,
                }
            ],
            model="gemma2-9b-it",
            stream=True
        )
        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")


