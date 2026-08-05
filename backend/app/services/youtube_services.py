'''This is to convert youtube video url into hash  https://www.youtube.com/watch?v=dQw4w9WgXcQ to dQw4w9WgXcQ'''
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str):
    parsed = urlparse(url)

    # Short URL: https://youtu.be/VIDEO_ID
    if parsed.netloc == "youtu.be":
        return parsed.path.lstrip("/")

    # Normal URL: https://www.youtube.com/watch?v=VIDEO_ID
    if "youtube.com" in parsed.netloc:
        return parse_qs(parsed.query).get("v", [None])[0]

    return None