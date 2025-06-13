import os
from openai import OpenAI

# Nếu các bạn dùng GroqAI
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='',
)

global applicationMessages

applicationMessages = []

while 1 == 1:
    print("Enter your message: ")
    userInput = input()
    if userInput == "exit":
        print("Exit")
        break
    else:

        applicationMessages.append(
            {
                "role": "user",
                "content": userInput,
            }
        )

        stream = client.chat.completions.create(
            messages = applicationMessages,
            model="gemma2-9b-it",
            stream=True,
            max_tokens=60
        )

        assistantMessage = ""

        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="") 
            assistantMessage += chunk.choices[0].delta.content or ""

        applicationMessages.append(
            {
                "role": "assistant",
                "content": assistantMessage,
            }
        )


