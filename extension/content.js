function getYouTubeVideoId() {
    const url = new URL(window.location.href);
    return url.searchParams.get("v");
}
const button = document.createElement("button");
button.id = "ai-learning-companion-button";
button.textContent = "🧠 AI Learning Companion";
button.style.padding = "10px 16px";
button.style.margin = "10px 0";
button.style.border = "none";
button.style.borderRadius = "18px";
button.style.background = "#0f0f0f";
button.style.color = "white";
button.style.fontSize = "14px";
button.style.fontWeight = "500";
button.style.cursor = "pointer";


const panel = document.createElement("div");
panel.id = "ai-learning-panel";
panel.style.position = "fixed";
panel.style.top = "80px";
panel.style.right = "20px";
panel.style.width = "320px";
panel.style.background = "white";
panel.style.color = "black";
panel.style.padding = "20px";
panel.style.borderRadius = "12px";
panel.style.boxShadow = "0 4px 20px rgba(0,0,0,0.3)";
panel.style.zIndex = "999999";
panel.style.display = "none";

panel.innerHTML = `
    <h2>🧠 AI Learning Companion</h2>

    <button id="summary-btn">📄 Summary</button>
    <button id="notes-btn">📝 Exam Notes</button>
    <button id="flashcard-btn">🃏 Flashcards</button>
    <button id="quiz-btn">❓ Quiz</button>
    <button id="question-btn">💬 Ask Questions</button>
`;

button.addEventListener("click", () => {

    const videoId = getYouTubeVideoId();
    fetch("http://127.0.0.1:8000/video-id", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        video_url: window.location.href
    })
})
.then(response => response.json())
.then(data => {
    console.log("Backend response:", data);
})
.catch(error => {
    console.error("Backend error:", error);
});

    alert("Video ID: " + videoId);

    if (panel.style.display === "none") {
        panel.style.display = "block";
    } else {
        panel.style.display = "none";
    }

});

const insertButton = () => {

    const target = document.querySelector("#top-level-buttons-computed");

    if (target && !document.querySelector("#ai-learning-companion-button")) {
        target.appendChild(button);
    }

};


document.getElementById("summary-btn").addEventListener("click", async () => {

    const summaryButton = document.getElementById("summary-btn");

    summaryButton.textContent = "⏳ Generating Summary...";
    summaryButton.disabled = true;

    try {

        const response = await fetch("http://127.0.0.1:8000/summary", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                video_url: window.location.href
            })
        });

        if (!response.ok) {
            throw new Error("Backend request failed");
        }

        const data = await response.json();

        console.log("Summary response:", data);

        panel.innerHTML = `
            <h2>📄 Summary</h2>

            <p>${data.summary}</p>

            <button id="back-btn">
                ← Back
            </button>
        `;

        document.getElementById("back-btn").addEventListener("click", () => {
            location.reload();
        });

    } catch (error) {

        console.error("Summary error:", error);

        panel.innerHTML = `
            <h2>❌ Error</h2>

            <p>Unable to generate summary.</p>

            <p>${error.message}</p>
        `;

    }

});

setInterval(insertButton, 1000);