from fastapi import FastAPI
from app.services.youtube_services import extract_video_id
from app.services.transcript_services import get_transcript

app = FastAPI()


''' "/" this refers to local host 127.0.0.1:8000'''
@app.get("/") 
def home():
    return {"message": "AI Learning Companion Backend Running"}


''' "/" this refers to local host 127.0.0.1:8000/video-id'''
@app.get("/video-id")
def get_video_id():
    url="https://www.youtube.com/watch?v=JtaOmwnR6AM"
    return extract_video_id(url)

@app.get("/transcript")
def transcript():
    video_id="JtaOmwnR6AM"
    return {
        "transcript":get_transcript(video_id)
    }

