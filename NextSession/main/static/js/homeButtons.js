var menuButton = document.querySelector('.main-menu');

menuButton.addEventListener('click', () => {
    var navList = document.querySelector(".nav-list");
    navList.classList.toggle("open-nav")
});