import os
from dotenv import load_dotenv
import google.generativeai as genai
from app.services.llm_formatting import parse_llm_json

load_dotenv()
genai.configure(
    api_key = os.getenv("GEMINI_API_KEY")
)
model=genai.GenerativeModel("gemini-2.5-flash")
def generate_summary(transcript):
    prompt = f"""
Summarize the following lecture.
Return only valid JSON with this format:
{{
  "short_summary": "...",
  "key_points": ["...", "..."]
}}
Do not wrap the response in markdown fences.
Transcript:
{transcript}
"""
    response=model.generate_content(prompt)
    parsed = parse_llm_json(response.text, lambda: {})
    if isinstance(parsed, str):
        return {"short_summary": parsed, "key_points": []}
    return parsed

    