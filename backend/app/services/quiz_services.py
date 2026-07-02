import os
from dotenv import load_dotenv
import google.generativeai as genai

from app.services.llm_formatting import parse_llm_json

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(transcript):

    prompt = f"""
    Generate 10 multiple choice questions.

    Return only valid JSON.

    Format:

    [
      {{
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "..."
      }}
    ]

    Do not wrap the response in markdown fences.

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    return parse_llm_json(response.text, lambda: [])