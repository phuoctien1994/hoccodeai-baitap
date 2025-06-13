from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='',
)

print("Nhập bài tập lập trình cần giải: ")
userInput = input()

chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": "Hãy giải giúp tôi bài tập với 1 số yêu cầu như sau:"
                "- Ngôn ngữ lập trình python"
                "- Kết quả trả về là 1 đoạn code python hoàn chỉnh, có thể copy toàn bộ nội dung và chạy ngay mà không bị lỗi"
                "- Tôi cần đoạn code chạy được ngay, có print ra console để người dùng biết đề bài, cần nhập thông tin gì vào"
                "- Không cần giải thích, không cần ```python"
                "- Không cần ```python hoặc ```"
                ,
            },
            {
                "role": "user",
                "content": "Đề bài: " + "\n" + userInput,
            }
        ],
        model="gemma2-9b-it"
    )

result = chat_completion.choices[0].message.content

with open("result_baitapj_2_5.py", "w", encoding="utf-8") as file:
    file.write(result)
    print(result)
    print('complete')