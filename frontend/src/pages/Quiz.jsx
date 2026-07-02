import { useState } from "react";
import { fetchQuiz } from "../services/api";

export default function Quiz() {
  const [videoUrl, setVideoUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(false);
  const [revealedAnswers, setRevealedAnswers] = useState({});

  async function handleGenerate() {
    setLoading(true);
    try {
      const q = await fetchQuiz(videoUrl);
      setQuiz(Array.isArray(q) ? q : []);
      setRevealedAnswers({});
    } catch (err) {
      setQuiz({ error: "Could not load quiz. Is backend running?" });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="study-page">
      <section className="study-hero">
        <p className="eyebrow">Quiz</p>
        <h2>Practice with one question at a time.</h2>
        <p>Enter a YouTube URL and reveal each answer only after you try the question.</p>
      </section>

      <section className="input-panel">
        <input
          type="text"
          placeholder="Paste YouTube URL"
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
          className="study-input"
        />

        <div className="study-actions">
          <button onClick={handleGenerate} disabled={loading} className="study-button">
            {loading ? "Working..." : "Generate Quiz"}
          </button>
        </div>
      </section>

      <section className="results-panel">
        <div className="section-heading">
          <h3>Questions</h3>
          <span>{Array.isArray(quiz) ? `${quiz.length} questions` : "Ready when you are"}</span>
        </div>

        {quiz && quiz.error ? (
          <div className="empty-state">{quiz.error}</div>
        ) : !Array.isArray(quiz) || !quiz.length ? (
          <div className="empty-state">No quiz available yet. Add a URL and generate one.</div>
        ) : (
          <div className="quiz-list">
            {quiz.map((q, i) => {
              const isRevealed = Boolean(revealedAnswers[i]);
              return (
                <article key={i} className="quiz-card">
                  <div className="quiz-card-top">
                    <span className="card-label">Question {i + 1}</span>
                    <button
                      type="button"
                      className="answer-toggle"
                      onClick={() => setRevealedAnswers((current) => ({ ...current, [i]: !current[i] }))}
                    >
                      {isRevealed ? "Hide answer" : "Show answer"}
                    </button>
                  </div>

                  <h4>{q.question || `Question ${i + 1}`}</h4>

                  <div className="options-grid">
                    {(q.options || q.choices || []).map((option, optionIndex) => (
                      <div key={optionIndex} className="option-pill">
                        {option}
                      </div>
                    ))}
                  </div>

                  {isRevealed && <div className="quiz-answer">Correct answer: {q.answer || "Not provided"}</div>}
                </article>
              );
            })}
          </div>
        )}
      </section>
    </div>
  );
}
