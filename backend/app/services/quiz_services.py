import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(transcript):

    prompt = f"""
    Generate 10 multiple choice questions.

    Return ONLY valid JSON.

    Format:

    [
      {{
        "question":"...",
        "options":[
          "A",
          "B",
          "C",
          "D"
        ],
        "answer":"..."
      }}
    ]

    Transcript:
    {transcript}
    """

    response = model.generate_content(prompt)

    return response.text