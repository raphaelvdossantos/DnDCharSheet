var menuButton = document.querySelector('#menu-button');
menuButton.addEventListener('click', () => {
    var menuNav = document.querySelector("#menu");
    menuNav.classList.add("menu-open");
});

var closeButton = document.querySelector('#close');
closeButton.addEventListener('click', () => {
    var menuNav = document.querySelector("#menu");
    menuNav.classList.remove("menu-open");
});


var optionsButtons = document.querySelectorAll('.character-menu');
optionsButtons.forEach(element => {
    element.addEventListener('click', () => {
        var options = element.parentElement.querySelector("#options-list");
        options.classList.toggle("options-open")
        
    });
});
