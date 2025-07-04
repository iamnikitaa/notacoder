document.addEventListener('DOMContentLoaded', () => {
    console.log('Custom script.js loaded successfully!');
    const messages = document.querySelectorAll('.message');

    messages.forEach(msg => {
        const text = msg.textContent.trim().toLowerCase();
        if (text.includes('correct') || text.includes('🎉')) {
            console.log('Correct answer detected. Launching confetti!');

            confetti({
                particleCount: 150,
                spread: 100,
                origin: { y: 0.6 }
            });
        }
    });
    const challengeForm = document.getElementById('challenge-submission-form');
    if (challengeForm) {
        challengeForm.addEventListener('submit', function (event) {
            event.preventDefault(); 
            console.log('Challenge form submitted!'); 
        });
    }
});
