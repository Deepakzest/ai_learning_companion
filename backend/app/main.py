from pydantic import BaseModel


class VideoRequest(BaseModel):
    video_url: str

from fastapi import FastAPI
from app.services.youtube_services import extract_video_id
from app.services.transcript_services import get_transcript
from app.services.summary_services import generate_summary
from app.services.flashcard_services import generate_flashcards
from app.services.quiz_services import generate_quiz
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware #connects backend and fronted//

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

''' "/" this refers to local host 127.0.0.1:8000'''
@app.get("/") 
def home():
    return {"message": "AI Learning Companion Backend Running"}


''' "/" this refers to local host 127.0.0.1:8000/video-id'''
@app.post("/video-id")
def get_video_id(data:VideoRequest):
    url=extract_video_id(data.video_url)
    return extract_video_id(url)

@app.post("/transcript")
def transcript(data:VideoRequest):
    video_id=extract_video_id(data.video_url)
    return {
        "transcript":get_transcript(video_id)
    }
@app.post("/summary")
def summary(data:VideoRequest):
    video_id=extract_video_id(data.video_url)
    transcript=get_transcript(video_id)
    summary_text=generate_summary(transcript)
    return {
        "summary":summary_text
    }
@app.post("/flashcards")
def flashcards(data:VideoRequest):
    video_id=extract_video_id(data.video_url)
    transcript=get_transcript(video_id)
    cards=generate_flashcards(transcript)
    return {
        "flashcards":cards
    }
@app.post("/quiz")
def quiz(data:VideoRequest):
    video_id=extract_video_id(data.video_url)
    transcript=get_transcript(video_id)
    quiz_data=generate_quiz(transcript)
    return{
        "quiz":quiz_data
    }