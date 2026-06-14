import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
model=genai.GenerativeModel("gemini-2.5-flash")

def generate_flashcards(transcript):
    prompt =f""" Generate 10 flashcard.
    return only valid JSON.
    Format:
    [
    {
        {
            "question":" ",
            "answer":" "
        }
    }]
    Transcript:{transcript}"""
    response=model.generate_content(prompt)
    return response.text