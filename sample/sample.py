from markitdown import MarkItDown
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 警告を無効化

session = requests.Session()
'''
session.proxies = {
    "http": "http://example.com:8888",
    "https": "https://example.com:8888"
}
'''

# より詳細なヘッダー設定
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://sb-proust001.discover-news.tokyo/",
    "Cache-Control": "max-age=0",
    # 既存のヘッダーに加えて
    "Origin": "https://sb-proust001.discover-news.tokyo",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty"
})

session.verify = False  # SSL検証を無効化

url = "https://sb-proust001.discover-news.tokyo/ab/best_deodorant_v3?utm_creative=uz_4cr_300_kimu_0501_.jpg"

# 直接requestsを使用してテスト
try:
    response = session.get(url)
    print(f"Status Code: {response.status_code}")
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# markitdownを使用
try:
    markitdown = MarkItDown(requests_session=session)
    result = markitdown.convert(url)
    print("\nMarkitdown result:")
    print(result.text_content)
except Exception as e:
    print(f"\nMarkitdown Error: {e}")