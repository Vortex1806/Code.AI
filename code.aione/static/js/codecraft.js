const submitBtn = document.querySelector('.submit-btn');
const inputField = document.querySelector('.codecraft-input');
const responseContainer = document.querySelector('.output-container');
const languageSelect = document.querySelector('.language-select');
const loadingIndicator = document.querySelector('.loading-indicator');
loadingIndicator.style.display = 'none';


submitBtn.addEventListener('click', async () => {
    const inputText = inputField.value;
    responseContainer.innerHTML = "";
    loadingIndicator.style.display = 'block';
    try {
        if (languageSelect.value == 'python') {
            const response = await fetch('http://127.0.0.1:4000/codecraftpy', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputText }),
                mode: 'cors'
            });
            const data = await response.json();
            responseContainer.innerHTML = data.response;
        } else if (languageSelect.value == 'javascript') {
            const response = await fetch('http://127.0.0.1:4000/codecraftjs', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputText }),
                mode: 'cors'
            });
            const data = await response.json();
            responseContainer.innerHTML = data.response;
        }
        else if (languageSelect.value == 'C') {
            const response = await fetch('http://127.0.0.1:4000/codecraftc', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputText }),
                mode: 'cors'
            });
            const data = await response.json();
            responseContainer.innerHTML = data.response;
        }
        else if (languageSelect.value == 'cpp') {
            const response = await fetch('http://127.0.0.1:4000/codecraftcpp', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputText }),
                mode: 'cors'
            });
            const data = await response.json();
            responseContainer.innerHTML = data.response;
        }
        else if (languageSelect.value == 'java') {
            const response = await fetch('http://127.0.0.1:4000/codecraftjava', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: inputText }),
                mode: 'cors'
            });
            const data = await response.json();
            responseContainer.innerHTML = data.response;
        }


    } catch (error) {
        console.error('Error fetching response from API:', error);
    }
    loadingIndicator.style.display = 'none';
});
