import axios from "axios";

// Centralized API client for communicating with the backend server.
// Change API_BASE if your backend runs elsewhere.
const API_BASE = "http://127.0.0.1:8000";

// Send the YouTube URL to backend /summary endpoint and return summary text.
export async function fetchSummary(videoUrl) {
  // axios.post sends JSON body to backend; backend reads `video_url` field.
  const resp = await axios.post(`${API_BASE}/summary`, { video_url: videoUrl });
  return resp.data.summary;
}

// Send the YouTube URL to backend /flashcards endpoint and return cards.
export async function fetchFlashcards(videoUrl) {
  const resp = await axios.post(`${API_BASE}/flashcards`, { video_url: videoUrl });
  return resp.data.flashcards;
}

// Fetch quiz from backend.
export async function fetchQuiz(videoUrl) {
  const resp = await axios.post(`${API_BASE}/quiz`, { video_url: videoUrl });
  return resp.data.quiz;
}

// Fetch transcript from backend. Backend currently returns a default transcript.
export async function fetchTranscript() {
  const resp = await axios.post(`${API_BASE}/transcript`,{video_url: videoUrl});
  return resp.data.transcript;
}

export default {
  fetchSummary,
  fetchFlashcards,
  fetchQuiz,
  fetchTranscript,
};
