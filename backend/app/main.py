from pydantic import BaseModel


class VideoRequest(BaseModel):
    video_url: str

from fastapi import FastAPI
from app.services.youtube_services import extract_video_id
from app.services.transcript_services import get_transcript
from app.services.summary_services import generate_summary
from app.services.flashcard_services import generate_flashcards
from app.services.quiz_services import generate_quiz
from app.services.examnotes_services import generate_exam_notes
import os
import tempfile

from fastapi.responses import FileResponse
from app.services.pdf_service import generate_exam_notes_pdf
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
def get_video_id(data: VideoRequest):
    print("Received URL:", data.video_url)
    video_id = extract_video_id(data.video_url)
    print("Extracted video ID:", video_id)
    return {
        "video_id": video_id
    }
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
@app.post("/exam-notes")
def exam_notes(data: VideoRequest):
    video_id = extract_video_id(data.video_url)
    transcript = get_transcript(video_id)
    notes = generate_exam_notes(transcript)

    return {
        "exam_notes": notes
    }
@app.post("/exam-notes/pdf")
def exam_notes_pdf(data: VideoRequest):

    video_id = extract_video_id(data.video_url)

    transcript = get_transcript(video_id)

    notes = generate_exam_notes(transcript)

    # Create a temporary PDF file
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    temp_file.close()

    generate_exam_notes_pdf(
        notes,
        temp_file.name
    )

    return FileResponse(
        temp_file.name,
        media_type="application/pdf",
        filename="exam_notes.pdf"
    )