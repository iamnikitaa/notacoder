document.addEventListener('DOMContentLoaded', (event) => {

    console.log('Custom script.js loaded successfully!');
    const challengeForm = document.getElementById('challenge-submission-form'); // Make sure your form has this ID

    if (challengeForm) {
        console.log('Challenge submission form found.');

        challengeForm.addEventListener('submit', function(event) {
            event.preventDefault(); 

            console.log('Challenge form submitted! AJAX logic will go here.');

            
        });
    }
}); 