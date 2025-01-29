// Toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

// Add animations to elements
document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('.animate');
    elements.forEach(element => {
        element.classList.add('animate__animated', 'animate__fadeInUp');
    });
});
