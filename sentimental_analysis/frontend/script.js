function analyzeSentiment() {
  const text = document.getElementById("inputText").value.trim();
  const resultEl = document.getElementById("result");

  if (!text) {
    resultEl.textContent = "⚠ Please type something first!";
    resultEl.className = "result";
    return;
  }

  resultEl.textContent = "🔍 Analyzing mood...";
  resultEl.className = "result";

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        resultEl.textContent = "❌ Error: " + data.error;
        resultEl.className = "result";
      } else {
        if (data.sentiment.toLowerCase() === "positive") {
          resultEl.textContent = "😊 Positive Mood Detected!";
          resultEl.className = "result positive";
        } else {
          resultEl.textContent = "☹ Negative Mood Detected!";
          resultEl.className = "result negative";
        }
      }
    })
    .catch(err => {
      resultEl.textContent = "⚠ Could not connect to API.";
      resultEl.className = "result";
      console.error(err);
    });
}