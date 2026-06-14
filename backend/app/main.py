from fastapi import FastAPI
from app.services.youtube_services import extract_video_id
from app.services.transcript_services import get_transcript
from app.services.summary_services import generate_summary
from app.services.flashcard_services import generate_flashcards
from app.services.quiz_services import generate_quiz
app = FastAPI()


''' "/" this refers to local host 127.0.0.1:8000'''
@app.get("/") 
def home():
    return {"message": "AI Learning Companion Backend Running"}


''' "/" this refers to local host 127.0.0.1:8000/video-id'''
@app.get("/video-id")
def get_video_id():
    url="https://www.youtube.com/watch?v=5OdVJbNCSso"
    return extract_video_id(url)

@app.get("/transcript")
def transcript():
    video_id="JtaOmwnR6AM"
    return {
        "transcript":get_transcript(video_id)
    }
@app.get("/summary")
def summary():
    video_id="5OdVJbNCSso"
    transcript=get_transcript(video_id)
    summary=generate_summary(transcript)
    return {
        "Summary":summary
    }
@app.get("/flashcards")
def flashcards():
    video_id=get_video_id()
    transcript=get_transcript(video_id)
    cards=generate_flashcards(transcript)
    return {
        "flashcards":cards
    }
@app.get("/quiz")
def quiz():
    video_id=get_video_id()
    transcript=get_transcript(video_id)
    quiz_data=generate_quiz(transcript)
    return{
        "quiz":quiz_data
    }