const submitBtn = document.querySelector('.submit-btn');
const inputField = document.querySelector('.input-container');
const languageSelect = document.querySelector('.language-select');
const responseContainer = document.querySelector('.output-container');
const loadingIndicator = document.querySelector('.loading-indicator');
loadingIndicator.style.display = 'none';

submitBtn.addEventListener('click', async () => {
    const inputText = inputField.value;
    const language = languageSelect.value;
    responseContainer.innerHTML = "";
    loadingIndicator.style.display = 'block';
    if (!language) {
        alert('Please select a language before submitting.');
        return;
    }
    try {
        const response = await fetch('http://127.0.0.1:4000/transcode', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: inputText, language: language }),
            mode: 'cors'
        });
        const data = await response.json();
        responseContainer.innerHTML = data.response;
    } catch (error) {
        console.error('Error fetching response from API:', error);
    }
    loadingIndicator.style.display = 'none';
});