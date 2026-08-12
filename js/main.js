/**
 * Abu Haider Maintenance - Core Application Engine & Global Controls
 */

// Global Config
window.ABU_HAIDER_CONFIG = {
  whatsappNumber: "905399118999",
  whatsappMessage: encodeURIComponent("مرحبًا أبو حيدر، أريد الاستفسار عن خدمة صيانة جهازي.")
};

document.addEventListener('DOMContentLoaded', () => {
  // Preloader Hide
  const preloader = document.querySelector('.preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        preloader.classList.add('hidden');
      }, 500);
    });
    // Fallback if load already fired
    setTimeout(() => {
      preloader.classList.add('hidden');
    }, 1200);
  }

  // Back to Top Button Handler
  const backToTopBtn = document.querySelector('.back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('active');
      } else {
        backToTopBtn.classList.remove('active');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Setup WhatsApp Links
  const whatsappLinks = document.querySelectorAll('.whatsapp-link');
  whatsappLinks.forEach(link => {
    link.href = `https://wa.me/${window.ABU_HAIDER_CONFIG.whatsappNumber}?text=${window.ABU_HAIDER_CONFIG.whatsappMessage}`;
    link.target = "_blank";
  });
});
