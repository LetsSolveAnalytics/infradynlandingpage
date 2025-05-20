const ctaFooter = document.getElementById('ctaFooter');

window.addEventListener('scroll', () => {
    const scrollBottom = window.innerHeight + window.scrollY;
    const docHeight = document.body.offsetHeight;

    // If user is near the bottom (within 50px), hide the footer
    if (scrollBottom >= docHeight - 50) {
        ctaFooter.style.opacity = '0';
        ctaFooter.style.pointerEvents = 'none';
    } else {
        ctaFooter.style.opacity = '1';
        ctaFooter.style.pointerEvents = 'auto';
    }
});

