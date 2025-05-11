function checkAnswer() {
    const input = document.getElementById('user-input').value.trim().toLowerCase();
    const response = document.getElementById('response');
  
    if (input === "immaculate") {
      response.textContent = "✅ immaculate vibes only. slay confirmed.";
      response.style.color = "#008000";
    } else {
      response.textContent = "🚫 uh oh. try again. that ain't it.";
      response.style.color = "#d00000";
    }
  }
  