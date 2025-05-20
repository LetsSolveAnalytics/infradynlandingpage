let currentStep = 1;

function nextStep() {
    const steps = document.querySelectorAll('.step');
    if (currentStep < steps.length) {
        steps[currentStep - 1].classList.remove('active');
        steps[currentStep].classList.add('active');
        document.getElementById(`dot${currentStep}`).classList.add('active');
        currentStep++;
    }
}

function selectOption(element, inputId, value) {
    document.querySelectorAll(`[name="${inputId}"]`).forEach(input => input.value = value);
    document.querySelectorAll(`.step[data-step="${currentStep}"] .card-option`).forEach(el => el.classList.remove('selected'));
    element.classList.add('selected');
    document.getElementById(inputId).value = value;
    document.getElementById(`nextBtn${currentStep}`).disabled = false;
}

document.getElementById('demoForm').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Form submitted successfully!');
});