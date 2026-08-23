import { useState } from "react";
import { fetchSummary,downloadExamNotesPDF } from "../services/api";

export default function Summary() {
  const [videoUrl, setVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState(null);
  const [pdfLoading, setPdfLoading] = useState(false);
  async function handleGenerate() {
    setLoading(true);
    try {
      const data = await fetchSummary(videoUrl);
      setSummary(data);
    } catch (err) {
      setSummary({ short_summary: "Error: could not get summary. Is backend running?", key_points: [] });
    } finally {
      setLoading(false);
    }
  }
  async function handleDownloadPDF() {
  if (!videoUrl.trim()) {
    alert("Please enter a YouTube URL first.");
    return;
  }

  setPdfLoading(true);

  try {
    await downloadExamNotesPDF(videoUrl);
  } catch (err) {
    console.error(err);
    alert("Could not generate the PDF. Is the backend running?");
  } finally {
    setPdfLoading(false);
  }
}

  return (
    <div className="study-page">
      <section className="study-hero">
        <p className="eyebrow">Summary</p>
        <h2>Read the lecture in a structured view.</h2>
        <p>Generate a concise summary with the key points grouped neatly below.</p>
      </section>

      <section className="input-panel">
      <input
        type="text"
        placeholder="Paste YouTube URL here"
        value={videoUrl}
        onChange={(e) => setVideoUrl(e.target.value)}
        className="study-input"
      />

      <div className="study-actions">
  <button
    onClick={handleGenerate}
    disabled={loading}
    className="study-button"
  >
    {loading ? "Working..." : "Generate Summary"}
  </button>

  <button
    onClick={handleDownloadPDF}
    disabled={pdfLoading}
    className="study-button"
  >
    {pdfLoading ? "Creating PDF..." : "📄 Generate Exam Notes PDF"}
  </button>
</div>
      </section>

      <section className="results-panel">
        <div className="section-heading">
          <h3>Summary</h3>
          <span>{summary ? "Generated" : "Ready when you are"}</span>
        </div>

        {!summary ? (
          <div className="empty-state">No summary yet. Enter a URL and generate one.</div>
        ) : (
          <div className="summary-layout">
            <article className="summary-card summary-highlight">
              <p className="card-label">Short summary</p>
              <p>{summary.short_summary || "No summary text returned."}</p>
            </article>

            <article className="summary-card">
              <p className="card-label">Key points</p>
              {Array.isArray(summary.key_points) && summary.key_points.length ? (
                <ul className="key-point-list">
                  {summary.key_points.map((point, index) => (
                    <li key={index}>{point}</li>
                  ))}
                </ul>
              ) : (
                <p className="muted">No key points returned.</p>
              )}
            </article>
          </div>
        )}
      </section>
    </div>
  );
}
