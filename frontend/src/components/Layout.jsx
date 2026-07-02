import { Link } from "react-router-dom";
import "../App.css";

// Simple layout with a top navigation bar and content area.
export default function Layout({ children }) {
  return (
    <div className="app-shell">
      <header className="topbar">
        <nav className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/summary">Summary</Link>
          <Link to="/flashcards">Flashcards</Link>
          <Link to="/quiz">Quiz</Link>
        </nav>
      </header>

      <main id="center">{children}</main>

      <div id="spacer" />
    </div>
  );
}
