function openSlideMenu() {
    document.getElementById('menu').style.width = '400px';
    document.getElementById('menu-list').style.opacity = '1';
}

function closeSlideMenu() {
    document.getElementById('menu').style.width = '0px';
    document.getElementById('menu-list').style.opacity = '0';
}

function openOptionsMenu() {
    document.getElementById('options-list').style.height = '19px';
    document.getElementById('character-menu').onclick = function() {
        closeOptionsMenu();
    };
}

function closeOptionsMenu() {
    document.getElementById('options-list').style.height = '0';
    document.getElementById('character-menu').onclick = function() {
        openOptionsMenu();
    };
}
