/**
 * Abu Haider Maintenance - Customer Testimonials Touch & Auto Slider
 */
document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.testimonials-slider');
  const slides = document.querySelectorAll('.testimonial-slide');
  const prevBtn = document.querySelector('.slider-btn-prev');
  const nextBtn = document.querySelector('.slider-btn-next');
  const dotsContainer = document.querySelector('.slider-dots');

  if (!slider || slides.length === 0) return;

  let currentIndex = 0;
  let autoSlideTimer = null;

  // Create Indicators/Dots
  slides.forEach((_, idx) => {
    const dot = document.createElement('div');
    dot.className = `slider-dot ${idx === 0 ? 'active' : ''}`;
    dot.addEventListener('click', () => goToSlide(idx));
    dotsContainer?.appendChild(dot);
  });

  const dots = document.querySelectorAll('.slider-dot');

  function updateSlider() {
    slides.forEach((slide, idx) => {
      slide.style.transform = `translateX(${(idx - currentIndex) * 100}%)`;
      slide.classList.toggle('active', idx === currentIndex);
    });

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === currentIndex);
    });
  }

  function goToSlide(index) {
    currentIndex = (index + slides.length) % slides.length;
    updateSlider();
    resetAutoSlide();
  }

  function nextSlide() {
    goToSlide(currentIndex + 1);
  }

  function prevSlide() {
    goToSlide(currentIndex - 1);
  }

  nextBtn?.addEventListener('click', nextSlide);
  prevBtn?.addEventListener('click', prevSlide);

  function startAutoSlide() {
    autoSlideTimer = setInterval(nextSlide, 5000);
  }

  function resetAutoSlide() {
    clearInterval(autoSlideTimer);
    startAutoSlide();
  }

  updateSlider();
  startAutoSlide();
});
