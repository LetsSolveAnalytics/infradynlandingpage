function showProduct(id) {
    const tabs = document.querySelectorAll(".tab-button");
    const contents = document.querySelectorAll(".product-content");

    tabs.forEach(tab => tab.classList.remove("active"));
    contents.forEach(content => content.classList.remove("active"));

    document.getElementById(id).classList.add("active");
    event.target.classList.add("active");
  }