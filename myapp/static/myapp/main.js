document.addEventListener('DOMContentLoaded', function () {
    var header = document.querySelector('.header');
    var menuToggle = document.querySelector('.menu-toggle');
    var navbar = document.querySelector('.navbar');
    var backToTop = document.querySelector('.back-to-top');

    if (header) {
        window.addEventListener('scroll', function () {
            header.classList.toggle('scrolled', window.scrollY > 20);
            if (backToTop) {
                backToTop.classList.toggle('visible', window.scrollY > 400);
            }
        });
    }

    if (menuToggle && navbar) {
        menuToggle.addEventListener('click', function () {
            var isOpen = navbar.classList.toggle('open');
            menuToggle.classList.toggle('active');
            menuToggle.setAttribute('aria-expanded', isOpen);
        });

        navbar.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                menuToggle.classList.remove('active');
                navbar.classList.remove('open');
                menuToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    if (backToTop) {
        backToTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    var currentPath = window.location.pathname.replace(/\/$/, '');
    document.querySelectorAll('.navbar a:not(.nav-cta)').forEach(function (link) {
        var href = link.getAttribute('href').replace(/\/$/, '');
        if (currentPath === href || currentPath.endsWith(href)) {
            link.classList.add('active');
        }
    });

    if ('IntersectionObserver' in window) {
        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        document.querySelectorAll('.reveal').forEach(function (el) {
            revealObserver.observe(el);
        });
    } else {
        document.querySelectorAll('.reveal').forEach(function (el) {
            el.classList.add('visible');
        });
    }
});
