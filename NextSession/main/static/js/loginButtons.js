var menuButton = document.querySelector('#main-menu');
menuButton.addEventListener('click', () => {
    var menuNav = document.querySelector("#nav-bar");
    menuNav.classList.toggle("nav-bar-open")
});