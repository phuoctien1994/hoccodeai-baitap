import requests
from openai import OpenAI
from bs4 import BeautifulSoup

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='',
)

def get_article_text(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    article = soup.find("div", class_="sidebar-1")
    if article:
        text = article.get_text(separator="\n", strip=True)
        return text
    else:
        return "Không tìm thấy nội dung bài viết."

text = get_article_text('https://vnexpress.net/ai-co-the-dong-gop-130-ty-usd-cho-kinh-te-viet-nam-4898025.html')

print("Url nội dung về công nghệ, chuyển đổi số trên vnexpress để tóm tắt: ")
userInput = input()
stream = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": "Đóng vai trò là 1 chuyên gia khoa học, công nghệ về chuyển đổi số, hãy phân tính bài báo sau theo các mục đích sau giúp tôi:"
            "- Viết nội dung tóm tắt bằng tiếng việt"
            "- Nếu bài báo nội dụng khác chuyển đổi số vui lòng báo người dùng gửi lại link bài báo khác và kết thúc trả lời"
            "- Tóm tắt cho tôi những mục lớn, những nội dung mà tôi cần lưu ý"
            "- Tôi là 1 lập trình viên thì tin tức này ảnh hưởng gì đến tôi"
            "- Dự đoán giúp tôi những khả năng có thể xảy ra trong tương lai",
        },
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

