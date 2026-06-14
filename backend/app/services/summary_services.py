import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(
    api_key = os.getenv("GEMINI_API_KEY")
)
model=genai.GenerativeModel("gemini-2.5-flash")
def generate_summary(transcript):
    prompt=f""" 
summarize the following lecture.
give:
1.Short summary
2.Important key points
Transcript:{transcript}
"""
    response=model.generate_content(prompt)
    return response.text

    