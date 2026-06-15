import { useState } from "react";
function Home() {
    const[videoUrl,setVideoUrl]=useState("");// Stores the YouTube URL entered by the user.
// Initially empty when the page loads
    const generateSummary =() =>{
    console.log("Current URL:",videoUrl);
    };
    return (
    <div>
      <h1>AI Learning Companion</h1>

      <input
        type="text"
        placeholder="Paste youtube url"
        value={videoUrl}
        // Updates videoUrl whenever the user types in the textbox.
        onChange={(e) => { console.log("Typing:", e.target.value);
            setVideoUrl(e.target.value)}}
      />

      <button onClick={generateSummary}>
        Generate Summary
      </button>
      <h3>{videoUrl}</h3>
    </div>
  );
}

export default Home;