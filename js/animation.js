/**
 * Abu Haider Maintenance - Royal Frame Typewriter Animation & Scroll Reveal Engine
 */

// Royal Frame Typewriter Configuration & Logic
class TypewriterAnimation {
  constructor(element, text, options = {}) {
    this.element = element;
    this.text = text;
    this.typingSpeed = options.typingSpeed || 90;
    this.deletingSpeed = options.deletingSpeed || 45;
    this.delayBetween = options.delayBetween || 2500;
    this.delayStart = options.delayStart || 600;

    this.charIndex = 0;
    this.isDeleting = false;
    this.timer = null;

    if (this.element) {
      this.init();
    }
  }

  init() {
    this.element.textContent = '';
    setTimeout(() => this.type(), this.delayStart);
  }

  type() {
    const currentText = this.text.substring(0, this.charIndex);
    this.element.textContent = currentText;

    if (!this.isDeleting && this.charIndex < this.text.length) {
      this.charIndex++;
      this.timer = setTimeout(() => this.type(), this.typingSpeed);
    } else if (!this.isDeleting && this.charIndex === this.text.length) {
      this.isDeleting = true;
      this.timer = setTimeout(() => this.type(), this.delayBetween);
    } else if (this.isDeleting && this.charIndex > 0) {
      this.charIndex--;
      this.timer = setTimeout(() => this.type(), this.deletingSpeed);
    } else if (this.isDeleting && this.charIndex === 0) {
      this.isDeleting = false;
      this.timer = setTimeout(() => this.type(), 500);
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Royal Frame Typewriter Animation
  const typewriterTarget = document.querySelector('.typewriter-text');
  if (typewriterTarget) {
    const brandPhrase = typewriterTarget.getAttribute('data-text') || "أبو حيدر لتصليح الأجهزة والكمبيوتر";
    new TypewriterAnimation(typewriterTarget, brandPhrase, {
      typingSpeed: 100,
      deletingSpeed: 50,
      delayBetween: 2400
    });
  }

  // Scroll Reveal Animations via IntersectionObserver
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  
  if ('IntersectionObserver' in window) {
    const observerOptions = {
      threshold: 0.15,
      rootMargin: '0px 0px -40px 0px'
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback for older browsers
    revealElements.forEach(el => el.classList.add('active'));
  }
});
