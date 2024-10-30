function toggleMode() {
    const body = document.body;
    const sunIcon = document.querySelector('.toggle-switch .icon.sun');
    const moonIcon = document.querySelector('.toggle-switch .icon.moon');

    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        sunIcon.style.display = 'inline'; // Show sun icon
        moonIcon.style.display = 'none'; // Hide moon icon
        document.cookie = "dark_mode=false; path=/"; // Set cookie for light mode
    } else {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        sunIcon.style.display = 'none'; // Hide sun icon
        moonIcon.style.display = 'inline'; // Show moon icon
        document.cookie = "dark_mode=true; path=/"; // Set cookie for dark mode
    }
}
