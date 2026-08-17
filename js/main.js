// Mobile navigation toggle
(function () {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('site-nav');

    if (!toggle || !nav) {
        return;
    }

    function setOpen(open) {
        nav.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    toggle.addEventListener('click', function () {
        setOpen(!nav.classList.contains('open'));
    });

    // Close the menu after tapping a link so the target section is visible
    nav.addEventListener('click', function (event) {
        if (event.target.tagName === 'A') {
            setOpen(false);
        }
    });

    // Reset state when returning to the desktop layout
    window.addEventListener('resize', function () {
        if (window.innerWidth > 750) {
            setOpen(false);
        }
    });
})();
