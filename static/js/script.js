const navToggle = document.querySelector('.menu-toggle');
const navMenu = document.querySelector('.sidebar');
const menuIcon = navToggle.querySelector('i');

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




// Update main gallery image when thumbnail is clicked
function updateMainImage(imageUrl) {
    document.getElementById('mainImage').src = imageUrl;
}


