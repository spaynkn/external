import json
import random
import string
from datetime import datetime

# JSONファイル名
filename = "videos.json"

# 既存データを読み込み
try:
    with open(filename, "r") as f:
        videos = json.load(f)
except FileNotFoundError:
    videos = []

# ランダム20文字のタイトル生成
random_title = ''.join(random.choices(string.ascii_letters, k=20))

# 新しい動画データ
new_video = {
    "title": random_title,
    "duration": "00:03:15",
    "url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
    "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
    "start": 10
}

# 配列に追加
videos.append(new_video)

# JSONを書き込み
with open(filename, "w") as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print(f"[{datetime.now()}] videos.json を更新しました。")
