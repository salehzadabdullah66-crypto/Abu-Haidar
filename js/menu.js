/**
 * Abu Haider Maintenance - Header Scroll & Mobile Hamburger Navigation
 */
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.header');
  const hamburgerBtn = document.querySelector('.hamburger-btn');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileOverlay = document.querySelector('.mobile-nav-overlay');

  // Sticky Header Scroll Effect
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // Mobile Menu Toggle
  function toggleMobileMenu() {
    hamburgerBtn?.classList.toggle('active');
    mobileNav?.classList.toggle('open');
    mobileOverlay?.classList.toggle('open');
    document.body.style.overflow = mobileNav?.classList.contains('open') ? 'hidden' : '';
  }

  hamburgerBtn?.addEventListener('click', toggleMobileMenu);
  mobileOverlay?.addEventListener('click', toggleMobileMenu);

  // Close menu on link click
  const mobileLinks = document.querySelectorAll('.mobile-nav .nav-link');
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileNav?.classList.contains('open')) {
        toggleMobileMenu();
      }
    });
  });
});
