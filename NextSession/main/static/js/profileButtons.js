var sectionsInfo = document.querySelectorAll('.section-info');
sectionsInfo.forEach(element => {
    var openButton = element.querySelector(".info-button");
    var section = element.querySelector(".info-content");
    openButton.addEventListener("click", () => {
        openButton.classList.toggle("rotate-button");
        section.classList.toggle("open-section");
    })
    
});