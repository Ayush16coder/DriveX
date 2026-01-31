document.addEventListener('DOMContentLoaded', () => {

    // 1. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: Stop observing once revealed
                // observer.unobserve(entry.target); 
            }
        });
    }, {
        root: null,
        threshold: 0.15, // Trigger when 15% visible
        rootMargin: "0px 0px -50px 0px" // Offset slightly triggers
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // 2. Sticky Navbar & Auth Logic
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
                navbar.style.boxShadow = "0 10px 30px -10px rgba(0,0,0,0.1)";
                navbar.style.background = "rgba(255, 255, 255, 0.95)";
            } else {
                navbar.classList.remove('scrolled');
                navbar.style.boxShadow = "none";
                navbar.style.background = "rgba(255, 255, 255, 0.8)"; // softer default
            }
        });
    }

    // --- AUTH PAGE LOGIC ---
    const roleBtns = document.querySelectorAll('.role-btn');
    const currentRoleSpans = document.querySelectorAll('.current-role');
    const ownerFields = document.querySelectorAll('.owner-field');

    // Role Switching
    if (roleBtns.length > 0) {
        roleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all
                roleBtns.forEach(b => b.classList.remove('active'));
                // Add to clicked
                btn.classList.add('active');

                // Update text
                const role = btn.dataset.role; // 'renter' or 'owner'
                const roleName = role === 'owner' ? 'Owner' : 'Renter';

                currentRoleSpans.forEach(span => span.textContent = roleName);

                // Update Hidden Input for backend (Signup)
                const signupRoleInput = document.getElementById('role-input');
                if (signupRoleInput) signupRoleInput.value = role;

                // Update Hidden Input for backend (Login)
                const loginRoleInput = document.getElementById('login-role-input');
                if (loginRoleInput) loginRoleInput.value = role;

                // Show/Hide Owner Fields
                ownerFields.forEach(field => {
                    field.style.display = role === 'owner' ? 'block' : 'none';
                });
            });
        });
    }

    // Login/Signup Toggle
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    const toSignup = document.getElementById('switch-to-signup');
    const toLogin = document.getElementById('switch-to-login');

    if (loginForm && signupForm) {
        toSignup.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.classList.remove('active');
            signupForm.classList.add('active');
        });

        toLogin.addEventListener('click', (e) => {
            e.preventDefault();
            signupForm.classList.remove('active');
            loginForm.classList.add('active');
        });
    }
});
// Loading Animation
function hideLoader() {
    const loader = document.getElementById('loader-wrapper');
    if (loader && !loader.classList.contains('loaded')) {
        setTimeout(() => {
            loader.classList.add('loaded');
            setTimeout(() => {
                loader.style.display = 'none';
            }, 500);
        }, 500); // Shorter initial delay
    }
}

// 1. Run when everything is fully loaded
if (document.readyState === 'complete') {
    hideLoader();
} else {
    window.addEventListener('load', hideLoader);
}

// 2. Fallback: Run after 3 seconds no matter what
setTimeout(hideLoader, 3000);
