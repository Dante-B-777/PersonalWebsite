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

// Reveal sections as they scroll into view.
// Progressive enhancement: the CSS only hides anything once this script adds
// the js-reveal flag, and a failsafe timer reveals everything regardless, so
// a stalled observer can never leave the page blank.
(function () {
    var targets = document.querySelectorAll('.section, .project-hero');

    if (!targets.length || !('IntersectionObserver' in window)) {
        return;
    }

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    var root = document.documentElement;

    targets.forEach(function (el) {
        el.classList.add('reveal');
    });
    root.classList.add('js-reveal');

    // Drops the hiding rule outright rather than relying on a transition to
    // finish, so content cannot be left stuck at zero opacity.
    function showAll() {
        root.classList.remove('js-reveal');
        targets.forEach(function (el) {
            el.classList.add('is-visible');
        });
    }

    var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                io.unobserve(entry.target);
            }
        });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.02 });

    targets.forEach(function (el) {
        io.observe(el);
    });

    // Failsafe: if the observer has not reported anything shortly after load,
    // reveal everything rather than risk showing a blank page.
    window.setTimeout(function () {
        if (!document.querySelector('.reveal.is-visible')) {
            showAll();
        }
    }, 1600);

    window.addEventListener('load', function () {
        window.setTimeout(function () {
            if (!document.querySelector('.reveal.is-visible')) {
                showAll();
            }
        }, 400);
    });
})();
