import { useState } from "react";
import { fetchFlashcards } from "../services/api";

export default function Flashcards() {
  const [videoUrl, setVideoUrl] = useState("");
  const [cards, setCards] = useState([]);
  const [loading, setLoading] = useState(false);
  const [openCard, setOpenCard] = useState(null);

  async function handleGenerate() {
    setLoading(true);
    try {
      const resp = await fetchFlashcards(videoUrl);
      setCards(Array.isArray(resp) ? resp : []);
      setOpenCard(null);
    } catch (err) {
      setCards([]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="study-page">
      <section className="study-hero">
        <p className="eyebrow">Flashcards</p>
        <h2>Tap a card to reveal the answer.</h2>
        <p>Generate study cards from a YouTube video and review them in a clean, interactive layout.</p>
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
          {loading ? "Working..." : "Generate Flashcards"}
        </button>
      </div>
      </section>

      <section className="results-panel">
        <div className="section-heading">
          <h3>Flashcards</h3>
          <span>{cards.length ? `${cards.length} cards` : "Ready when you are"}</span>
        </div>

        {!cards.length ? (
          <div className="empty-state">No flashcards yet. Enter a URL and generate them.</div>
        ) : (
          <div className="flashcard-grid">
            {cards.map((card, index) => {
              const isOpen = openCard === index;
              return (
                <button
                  key={index}
                  type="button"
                  className={`flashcard ${isOpen ? "is-open" : ""}`}
                  onClick={() => setOpenCard(isOpen ? null : index)}
                >
                  <span className="card-label">Question</span>
                  <div className="flashcard-content">
                    <p className="card-question">{card.question || `Question ${index + 1}`}</p>
                    <div className="card-answer-wrap">
                      {isOpen ? (
                        <p className="card-answer">{card.answer || "No answer provided."}</p>
                      ) : (
                        <p className="card-hint">Click to reveal the answer</p>
                      )}
                    </div>
                  </div>
                </button>
              );
            })}
          </div>
        )}
      </section>
    </div>
  );
}
