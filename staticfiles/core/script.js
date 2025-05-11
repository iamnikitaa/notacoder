document.querySelector(".login-btn").onclick = () => {
    alert("Redirecting to log in. Let's glow up your session 🌟");
};

document.querySelector(".guest-btn").onclick = () => {
    alert("You're in as a guest! No strings attached 💅");
};

const affirmations = [
    "You're doing amazing, sweetie 💖",
    "Your code slays, even if it breaks 🧠",
    "Debugging builds character ✨",
    "You’re literally built different 👾",
    "Shipping is better than perfect 🚀",
    "Your brain has the range 💅",
    "Tech baddie detected 🔥",
    "You got this, always ✨"
];

window.addEventListener('DOMContentLoaded', () => {
    console.log("JS loaded — selecting affirmation...");
    const vibe = document.getElementById("affirmation");
    if (vibe) {
        const randomAffirmation = affirmations[Math.floor(Math.random() * affirmations.length)];
        vibe.textContent = randomAffirmation;
    } else {
        console.warn("No #affirmation element found!");
    }
});
