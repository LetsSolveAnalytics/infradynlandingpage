function showProduct(slug) {
    // Remove active class from all buttons and content
    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.product-content').forEach(pc => pc.classList.remove('active'));

    // Add active class to selected
    document.querySelector(`.tab-button[onclick="showProduct('${slug}')"]`).classList.add('active');
    document.getElementById(slug).classList.add('active');
}