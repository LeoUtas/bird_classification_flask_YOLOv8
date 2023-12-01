// handle the typing effect
const text = "All models are wrong, but some are useful";
let index = 0;
const outputElement = document.getElementById('typing-text');

function type() {
    if (index < text.length) {
        outputElement.textContent += text.charAt(index);
        index++;
        setTimeout(type, 100);  // typing speed
    } else {
        setTimeout(erase, 1000);  // delay before erasing
    }
}

function erase() {
    if (index > 0) {
        outputElement.textContent = text.substring(0, index - 1);
        index--;
        setTimeout(erase, 100);  // erasing speed
    } else {
        setTimeout(type, 1000);  // delay before retyping
    }
}

window.onload = type;


// handle the animation effect
document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('.form');
    const loadingAnimation = document.getElementById('loading-animation');
    const resultDiv = document.querySelector('.result');
    const resultImage = document.querySelector('.result img');

    form.addEventListener('submit', () => {
        // hide the result div and show the loading animation when the form is submitted
        resultDiv.classList.add('hidden');
        loadingAnimation.classList.remove('hidden');
    });

    const observer = new MutationObserver((mutationsList, observer) => {
        for(let mutation of mutationsList) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'src') {
                // show the result div and hide the animation when the image source changes
                resultDiv.classList.remove('hidden');
                loadingAnimation.classList.add('hidden');
                break;
            }
        }
    });

    observer.observe(resultImage, { attributes: true });
});

