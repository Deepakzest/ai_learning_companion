import os

from dotenv import load_dotenv
import google.generativeai as genai

from app.services.llm_formatting import parse_llm_json

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_exam_notes(transcript):

    prompt = f"""
You are an expert educational content creator.

Convert the following YouTube lecture transcript into
exam-oriented study notes for a college student.

Focus only on information present in the transcript.
Do not invent information.

Return ONLY valid JSON in exactly this structure:

{{
    "title": "...",
    "overview": "...",
    "important_definitions": [
        {{
            "term": "...",
            "definition": "..."
        }}
    ],
    "key_concepts": [
        {{
            "concept": "...",
            "explanation": "..."
        }}
    ],
    "important_points": [
        "..."
    ],
    "comparisons": [
        {{
            "topic": "...",
            "points": [
                {{
                    "aspect": "...",
                    "first": "...",
                    "second": "..."
                }}
            ]
        }}
    ],
    "exam_questions": [
        {{
            "question": "...",
            "answer_points": [
                "..."
            ]
        }}
    ],
    "quick_revision": [
        "..."
    ]
}}

Rules:

1. Make the notes useful for university examinations.
2. Extract important definitions from the lecture.
3. Identify concepts that are likely to be important for exams.
4. Include comparisons only when the transcript contains comparable topics.
5. Generate possible exam questions based ONLY on the transcript.
6. Keep answers concise but useful for revision.
7. Do not add information that is not present in the transcript.
8. If a section is not applicable, return an empty list.
9. Do not use markdown.
10. Do not wrap the response in markdown code fences.

Transcript:

{transcript}
"""

    response = model.generate_content(prompt)

    parsed = parse_llm_json(response.text, lambda: {})

    if isinstance(parsed, str):
        return {
            "title": "Exam Notes",
            "overview": parsed,
            "important_definitions": [],
            "key_concepts": [],
            "important_points": [],
            "comparisons": [],
            "exam_questions": [],
            "quick_revision": []
        }

    return parsed