import requests
import urllib3
from markitdown import MarkItDown
import time  # 追加

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()

'''
session.proxies = {
    "https": "https://muroon.info:443:"
}
'''

# クッキーを保持するための辞書を追加
cookies = {
    # Cloudflareのクッキーを保持
    'cf_clearance': '',  # 実際の値は空白のままで良い
}

# ヘッダーの更新
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  # より新しいバージョンに更新
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://sb-proust001.discover-news.tokyo/",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
})

session.verify = False
session.cookies.update(cookies)

url = "https://sb-proust001.discover-news.tokyo/ab/best_deodorant_v3?utm_creative=uz_4cr_300_kimu_0501_.jpg"

def make_request():
    try:
        response = session.get(url)
        print(f"Status Code: {response.status_code}")
        print("\nResponse Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        
        # レスポンスのクッキーを保存
        if response.cookies:
            session.cookies.update(response.cookies)
            
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# 最初のリクエスト
response = make_request()

# Cloudflareのチャレンジが完了するまで待機
time.sleep(5)  # 5秒待機

print("\n")

# 2回目のリクエスト
response = make_request()

if response and response.status_code == 200:
    try:
        markitdown = MarkItDown(requests_session=session)
        result = markitdown.convert(url)
        print("\nMarkitdown result:")
        print(result.text_content)
    except Exception as e:
        print(f"\nMarkitdown Error: {e}")