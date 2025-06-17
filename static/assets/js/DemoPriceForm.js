let currentStep = 1;

// Ensure scroll to top of form on step change (for mobile)
function scrollToFormTop() {
  const form = document.getElementById('demoForm');
  if (form) {
    form.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}

// Update nextStep and prevStep to scroll on change
function nextStep() {
  const steps = document.querySelectorAll('.step');
  if (currentStep < steps.length) {
    steps[currentStep - 1].classList.remove('active');
    steps[currentStep].classList.add('active');
    document.getElementById(`dot${currentStep}`).classList.add('active');
    currentStep++;
    scrollToFormTop(); // added
  }
}

function prevStep() {
  const steps = document.querySelectorAll('.step');
  if (currentStep > 1) {
    steps[currentStep - 1].classList.remove('active');
    steps[currentStep - 2].classList.add('active');
    document.getElementById(`dot${currentStep - 1}`).classList.remove('active');
    currentStep--;
    scrollToFormTop(); // added
  }
}

function selectOption(element, inputId, value) {
  document.querySelectorAll(`[name="${inputId}"]`).forEach(input => input.value = value);
  document.querySelectorAll(`.step[data-step="${currentStep}"] .card-option`).forEach(el => el.classList.remove('selected'));
  element.classList.add('selected');
  document.getElementById(inputId).value = value;
  document.getElementById(`nextBtn${currentStep}`).disabled = false;
}

// document.getElementById('priceForm').addEventListener('submit', function (e) {
//   e.preventDefault();
//   alert('Form submitted successfully!');
// });

// document.getElementById('demoForm').addEventListener('submit', function (e) {
//     e.preventDefault();
//     alert('Form submitted successfully!');
// });