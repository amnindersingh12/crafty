/**
 * Getting Crafty - Main JavaScript
 * Handles header scroll, dropdowns, mobile menu, and cart
 */

document.addEventListener('DOMContentLoaded', () => {
    initHeader();
    initDropdowns();
    initMobileMenu();
    initMarquee();
    initScrollAnimations();
});

/**
 * Header - Transparent to solid on scroll
 */
function initHeader() {
    const header = document.getElementById('header');
    if (!header) return;

    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.setAttribute('data-scrolled', 'true');
        } else {
            header.setAttribute('data-scrolled', 'false');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Check initial state
}

/**
 * Navigation Dropdowns
 */
function initDropdowns() {
    const dropdowns = document.querySelectorAll('.nav-dropdown');

    dropdowns.forEach(dropdown => {
        const trigger = dropdown.querySelector('.nav-dropdown-trigger');

        trigger.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = dropdown.getAttribute('data-open') === 'true';

            // Close all dropdowns
            dropdowns.forEach(d => d.setAttribute('data-open', 'false'));

            // Toggle this dropdown
            dropdown.setAttribute('data-open', !isOpen);
            trigger.setAttribute('aria-expanded', !isOpen);
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', () => {
        dropdowns.forEach(d => {
            d.setAttribute('data-open', 'false');
            d.querySelector('.nav-dropdown-trigger')?.setAttribute('aria-expanded', 'false');
        });
    });
}

/**
 * Mobile Menu
 */
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const menu = document.getElementById('mobile-menu');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        const isActive = menu.classList.contains('active');
        menu.classList.toggle('active');
        toggle.setAttribute('aria-expanded', !isActive);

        // Prevent body scroll when menu is open
        document.body.style.overflow = isActive ? '' : 'hidden';
    });

    // Close menu when clicking a link
    menu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

/**
 * Update cart count badge
 */
function updateCartCount(count) {
    const badge = document.getElementById('cart-count');
    if (badge) {
        badge.textContent = count;
    }
}

/**
 * Add to cart with animation
 */
async function addToCart(productId, quantity = 1) {
    try {
        const response = await fetch('/api/cart/add/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product_id: productId, quantity }),
        });

        const data = await response.json();

        if (data.success) {
            updateCartCount(data.cart_count);
            return data;
        }
    } catch (error) {
        console.error('Error adding to cart:', error);
    }

    return null;
}

// Export for use in templates
window.GettingCrafty = {
    updateCartCount,
    addToCart,
};

/**
 * Wavy Marquee Animation
 */
function initMarquee() {
    const textPath = document.getElementById('marquee-text-path');
    if (!textPath) return;

    // Movement parameters
    const speed = 1.0; // From reference
    const repeatInterval = 760;

    // Start at -repeatInterval to ensure content enters from left seamlessly
    // Or use the initial value from HTML if present to match layout
    let initialOffset = parseFloat(textPath.getAttribute('startOffset')) || -repeatInterval;
    let offset = initialOffset;

    function animate() {
        // "animationDirection": "right" -> increment offset
        offset += speed;

        // Reset when we've moved one full cycle (0 is the "start" of the next cycle visually)
        if (offset >= 0) {
            offset -= repeatInterval;
        }

        textPath.setAttribute('startOffset', offset);
        requestAnimationFrame(animate);
    }

    // Respect reduced motion preference
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (!mediaQuery.matches) {
        requestAnimationFrame(animate);
    }
}

/**
 * Scroll Animations utilizing IntersectionObserver
 */
function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before element enters fully
        threshold: 0.05 // Trigger when even a small part is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add a small delay based on index if multiple items appear at once (optional manual staggering logic could go here)
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const elements = document.querySelectorAll('.reveal-on-scroll');
    elements.forEach(el => observer.observe(el));
}
