'''This is to convert youtube video url into hash  https://www.youtube.com/watch?v=dQw4w9WgXcQ to dQw4w9WgXcQ'''

from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str):
    query = urlparse(url)
    return parse_qs(query.query).get("v", [None])[0]