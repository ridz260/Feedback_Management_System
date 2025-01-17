document.getElementById('surveyForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const questions = document.getElementById('questions').value.split(',').map(q => q.trim());
    const start_date = document.getElementById('start_date').value;
    const end_date = document.getElementById('end_date').value;

    const response = await fetch('/surveys/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, questions, start_date, end_date }),
    });

    const data = await response.json();
    document.getElementById('message').innerText = data.message;
});

document.getElementById('responseForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const survey_id = document.getElementById('survey_id').value;
    const answers = document.getElementById('answers').value.split(',').map(a => a.trim());

    const response = await fetch('/responses/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ survey_id, answers }),
    });

    const data = await response.json();
    document.getElementById('message').innerText = data.message;
});