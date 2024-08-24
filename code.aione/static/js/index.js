
const learnButton = document.getElementById('learn-btn');
learnButton.addEventListener('click', function () {
    const sectionTwo = document.getElementById('section-two');
    sectionTwo.scrollIntoView({ behavior: 'smooth' });
});

const submitBtn = document.getElementById("submit-btn");
const emailInput = document.getElementById("hero-field");

submitBtn.addEventListener("click", () => {
    emailInput.value = 'Thanks for subscribing';
    emailInput.disabled = true;
    submitBtn.disabled = true;
});
