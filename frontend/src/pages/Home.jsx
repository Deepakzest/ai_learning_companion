import { Link } from "react-router-dom";

// Home is a friendly landing page that points to the different tools.
export default function Home() {
  return (
    <div>
      <h1>AI Learning Companion</h1>
      <p style={{ maxWidth: 720, margin: "12px auto" }}>
        Welcome — use the links above to access tools that turn YouTube lectures into summaries,
        flashcards, quizzes, and transcripts. Each tool talks to the backend server to do the heavy
        lifting.
      </p>

      <div style={{ display: "flex", gap: 12, justifyContent: "center", marginTop: 20 }}>
        {/* Big call-to-action buttons that navigate to each feature */}
        <Link to="/summary" style={{ padding: "10px 18px", background: "var(--accent)", color: "white", borderRadius: 8, textDecoration: "none" }}>Summary</Link>
        <Link to="/flashcards" style={{ padding: "10px 18px", background: "var(--accent-bg)", color: "var(--accent)", borderRadius: 8, textDecoration: "none" }}>Flashcards</Link>
        <Link to="/quiz" style={{ padding: "10px 18px", background: "var(--accent-bg)", color: "var(--accent)", borderRadius: 8, textDecoration: "none" }}>Quiz</Link>
        <Link to="/transcript" style={{ padding: "10px 18px", background: "var(--accent-bg)", color: "var(--accent)", borderRadius: 8, textDecoration: "none" }}>Transcript</Link>
      </div>
    </div>
  );
}