const items = document.querySelectorAll(".listing-item");

let current = 0;

items[current].classList.add("active");

function advance() {

    items[current].classList.remove("active");

    current = (current + 1) % items.length;

    items[current].classList.add("active");

    const delay = 5000 + (Math.random() * 300 - 150);

    setTimeout(advance, delay);
}

const initialDelay = 5000 + (Math.random() * 300 - 150);

setTimeout(advance, initialDelay);