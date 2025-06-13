
from openai import OpenAI
import re

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='',
)

def translate_vietnamese(textTranslate, writingType):

    prompt = "Dịch sang tiếng việt va lưu ý rằng bạn đang dịch 1 phần trong bài text của tôi, tôi sẽ ghép nhiều đoạn lại với nhau để có 1 bài dịch hoàn chỉnh. Đóng vai trò là 1 chuyên viên về database, hãy dịch nội dung này đúng ý nghĩa về database với giọng văn bình thường, sát nghĩa"

    if writingType == "humorousTone":
        prompt = "Dịch sang tiếng việt va lưu ý rằng bạn đang dịch 1 phần trong bài text của tôi, tôi sẽ ghép nhiều đoạn lại với nhau để có 1 bài dịch hoàn chỉnh. Đóng vai trò là 1 chuyên viên về database, hãy dịch nội dung đoạn văn sau một cách vui vẻ, thú vị và thân thiện, có pha " \
        "chút hóm hỉnh, hài hước."

    if writingType == "formalTone":
        prompt = "Dịch sang tiếng việt va lưu ý rằng bạn đang dịch 1 phần trong bài text của tôi, tôi sẽ ghép nhiều đoạn lại với nhau để có 1 bài dịch hoàn chỉnh. Đóng vai trò là 1 chuyên viên về database, hãy dịch giúp tôi nội dung này một cách trang trọng nhất, giọng văn để có thể" \
        "thuyết trình trước đám đông mục đích chia sẽ kiến thức về công nghệ"

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "user",
                "content": textTranslate,
            }
        ],
        model="gemma2-9b-it"
    )

    return chat_completion.choices[0].message.content

def SplitContent(content):
    max_chars = 1000
    sentences = re.split(r'(?<=[.!?])\s+', content)  # Tách văn bản thành các câu

    chunks = []
    current_chunk = ""

    for sentence in sentences:
    # Nếu thêm câu này vào sẽ vượt quá max_chars, thì lưu chunk hiện tại và bắt đầu chunk mới
        if len(current_chunk) + len(sentence) + 1 > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence

# Thêm phần còn lại
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

global content 
global result_normal
global result_humorousTone
global result_formalTone

result_normal = ""
result_humorousTone = ""
result_formalTone = ""

with open("engLish.txt", "r", encoding="utf-8") as file:
    content = file.read()

chunks = SplitContent(content)

# In ra từng đoạn
for idx, chunk in enumerate(chunks, 1):
    result_normal += translate_vietnamese(chunk, '')
    result_humorousTone += translate_vietnamese(chunk, 'humorousTone')
    result_formalTone += translate_vietnamese(chunk, 'formalTone')

with open("output_normal.txt", "w", encoding="utf-8") as file:
    file.write(result_normal)
    print('complete normal')

with open("output_humorousTone.txt", "w", encoding="utf-8") as file:
    file.write(result_humorousTone)
    print('complete humorousTone')

with open("output_formalTon.txt", "w", encoding="utf-8") as file:
    file.write(result_formalTone)
    print('complete formalTone')