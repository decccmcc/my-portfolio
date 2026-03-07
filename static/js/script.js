const navToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('.sidebar');
const menuIcon = navToggle.querySelector('i');
const pageTitle = document.querySelector('.page-title');
const pageRevealBlocks = document.querySelectorAll('.page-content-reveal');
const hasFeedbackMessage = document.querySelector('.message-success, .message-error');
const hasFormErrors = document.querySelector('.form-error, .form-errors');
const shouldSkipTitleAnimation = Boolean(hasFeedbackMessage || hasFormErrors);

// Toggle sidebar when hamburger is clicked
navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    menuIcon.classList.toggle('fa-bars');
    menuIcon.classList.toggle('fa-times');
});

// Close sidebar when clicking outside of it
document.addEventListener('click', (e) => {
    if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
        navMenu.classList.remove('active');
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    }
});

// Close sidebar when clicking a nav link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    });
});

// Typewriter effect for page title before content reveal
function runTitleTypewriter() {
    if (!pageTitle) {
        return;
    }

    if (shouldSkipTitleAnimation) {
        document.body.classList.remove('is-typing-title');
        document.body.classList.add('title-typed');
        return;
    }

    const originalText = pageTitle.textContent.trim();

    if (!originalText) {
        document.body.classList.add('title-typed');
        return;
    }

    if (pageRevealBlocks.length > 0) {
        document.body.classList.add('is-typing-title');
    }

    pageTitle.textContent = '';
    let charIndex = 0;

    const typeNextChar = () => {
        pageTitle.textContent += originalText.charAt(charIndex);
        charIndex += 1;

        if (charIndex < originalText.length) {
            setTimeout(typeNextChar, 30);
            return;
        }

        document.body.classList.remove('is-typing-title');
        document.body.classList.add('title-typed');
    };

    setTimeout(typeNextChar, 120);
}

runTitleTypewriter();




// Update main gallery image when thumbnail is clicked
function updateMainImage(imageUrl) {
    const mainImage = document.getElementById('mainImage');
    if (mainImage) {
        mainImage.src = imageUrl;
    }
}

// Gallery thumbnail click handler with keyboard support
document.addEventListener('DOMContentLoaded', () => {
    const thumbnailBtns = document.querySelectorAll('.gallery-thumb-btn');
    thumbnailBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const imageUrl = btn.getAttribute('data-image-url');
            if (imageUrl) {
                updateMainImage(imageUrl);
            }
        });
    });
});
