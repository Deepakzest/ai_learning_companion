# AI Learning Companion

AI Learning Companion is a FastAPI-based backend application that transforms  YouTube videos into interactive learning resources. By providing a YouTube video URL, users can automatically extract transcripts, generate concise summaries, create flashcards, and produce quizzes for effective learning.
The project encourages active learning by converting long educational videos into structured study materials.


## Features

- **YouTube Content Processing**: Extract and process educational content from YouTube videos
- **AI-Powered Study Materials**: 
  - Generate flashcards from video transcripts
  - Create interactive quizzes with multiple-choice questions
  - Produce concise summaries with key points
- **Interactive UI**: React-based frontend for seamless learning experience
- **RESTful API**: FastAPI backend for efficient content processing
- **LLM Integration**: Advanced language model formatting for structured output

## Project Structure

```
ai_learning_companion/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── main.py            # Application entry point
│   │   ├── routes/            # API endpoints
│   │   └── services/          # Business logic
│   │       ├── flashcard_services.py
│   │       ├── quiz_services.py
│   │       ├── summary_services.py
│   │       ├── transcript_services.py
│   │       ├── youtube_services.py
│   │       └── llm_formatting.py
│   └── requirements.txt        # Python dependencies
│
├── frontend/                   # React + Vite frontend
│   ├── src/
│   │   ├── components/        # Reusable React components
│   │   ├── pages/             # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── Flashcards.jsx
│   │   │   ├── Quiz.jsx
│   │   │   └── Summary.jsx
│   │   ├── services/          # API client
│   │   └── App.jsx
│   ├── package.json           # Node dependencies
│   └── vite.config.js         # Vite configuration
│
└── README.md                  # This file
```

## Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **pip** and **npm** package managers
- YouTube video URL for content processing

## Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

### Start the Backend Server

1. From the `backend` directory with virtual environment activated:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. API Documentation: `http://localhost:8000/docs` (Swagger UI)
<img width="1096" height="528" alt="image" src="https://github.com/user-attachments/assets/2637d979-afa4-4f5e-bd99-450addb2910a" />


### Start the Frontend Development Server

1. From the `frontend` directory:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173` (or as indicated by Vite)

<img width="1437" height="659" alt="image" src="https://github.com/user-attachments/assets/8f4f43a9-abaf-487b-8925-3f5953761525" />
<img width="414" height="677" alt="image" src="https://github.com/user-attachments/assets/9cdd0980-1522-4902-9f30-4bb517398c6e" />
<img width="852" height="903" alt="image" src="https://github.com/user-attachments/assets/11757ef1-4c3e-4a8b-8ea2-733aabd2558f" />
<img width="817" height="814" alt="image" src="https://github.com/user-attachments/assets/7bc09cf8-9497-4d54-be4d-8632136cfe5c" />





## API Endpoints

### Study Materials Generation

- **POST /flashcards** - Generate flashcards from a video
  - Body: `{ "video_url": "https://youtube.com/..." }`
  - Returns: Structured flashcard data

- **POST /quiz** - Generate quiz questions from a video
  - Body: `{ "video_url": "https://youtube.com/..." }`
  - Returns: Multiple-choice quiz questions

- **POST /summary** - Generate summary from a video
  - Body: `{ "video_url": "https://youtube.com/..." }`
  - Returns: `short_summary` and `key_points`

- **POST /transcript** - Extract transcript from a video
  - Body: `{ "video_url": "https://youtube.com/..." }`
  - Returns: Video transcript text

## Technology Stack

### Backend
- **FastAPI** - Modern web framework for building APIs
- **Python** - Backend programming language
- **LLM Integration** - Advanced language model for content generation(google gemini model-free)

### Frontend
- **React** - UI library
- **Vite** - Fast build tool and dev server
- **CSS** - Styling

## Key Features

### Flashcards
- Automatically generated from video content
- Structured Q&A format
- Interactive card display

### Quiz Generation
- Multiple-choice questions
- Auto-generated from video transcripts
- Progress tracking ready

### Summary Creation
- Concise summaries of video content
- Key points extraction
- Quick reference format

## Output Format

The backend ensures all LLM outputs are normalized into structured JSON before sending to the frontend:
- Flashcards: `{ "flashcards": [...] }`
- Quiz: `{ "questions": [...] }`
- Summary: `{ "short_summary": "...", "key_points": [...] }`

## Troubleshooting

### Backend Issues
- Ensure virtual environment is activated
- Check that all dependencies in `requirements.txt` are installed
- Verify API server is running on port 8000

### Frontend Issues
- Clear node_modules and reinstall: `npm install`
- Clear Vite cache: `rm -rf node_modules/.vite`
- Ensure backend is running before making API calls


