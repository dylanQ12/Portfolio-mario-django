document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.set-bg').forEach(function(elem) {
        var bg = elem.getAttribute('data-setbg');
        elem.style.backgroundImage = 'url(' + bg + ')';
    });
});