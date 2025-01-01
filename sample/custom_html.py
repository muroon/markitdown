# custom_html.py
from markitdown import MarkItDown
import requests

session = requests.Session()
session.proxies = {
    "http": "http://example.com:8888",
    "https": "https://example.com:8888"
}
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7"
})

markitdown = MarkItDown(requests_session=session)

#result = markitdown.convert("https://lifull.com/doc/2024/11/20241114_-youshiQA-.pdf")
#result = markitdown.convert("https://sb-proust001.discover-news.tokyo/ab/best_deodorant_v3?utm_creative=uz_4cr_300_kimu_0501_.jpg")
#result = markitdown.convert("https://www.yahoo.co.jp/")
#result = markitdown.convert("https://support.yahoo-net.jp/noscript")
result = markitdown.convert("https://www.sponichi.co.jp/")
print(result.text_content)

