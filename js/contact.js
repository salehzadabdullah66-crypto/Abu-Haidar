/**
 * Abu Haider Maintenance - Form Handling & Interactive Success Modal
 */
document.addEventListener('DOMContentLoaded', () => {
  const bookingForm = document.getElementById('bookingForm');
  const contactForm = document.getElementById('contactForm');

  // Success Modal Creator
  function showSuccessModal(name, serviceName) {
    const successModal = document.createElement('div');
    successModal.className = 'modal-overlay success-modal active';
    successModal.innerHTML = `
      <div class="modal-content" style="text-align: center;">
        <div style="width: 75px; height: 75px; border-radius: 50%; background: rgba(34, 197, 94, 0.15); border: 2px solid #22c55e; color: #22c55e; display: flex; align-items: center; justify-content: center; font-size: 2.2rem; margin: 0 auto 1.5rem auto;">
          <i class="fas fa-check"></i>
        </div>
        <h3 style="font-size: 1.6rem; font-weight: 800; color: var(--color-gold); margin-bottom: 0.8rem;">تم استلام طلبك بنجاح!</h3>
        <p style="color: var(--text-muted); line-height: 1.7; margin-bottom: 1.8rem;">
          أهلاً بك يا <strong style="color: var(--text-main);">${name}</strong>، تم تسجيل طلب صيانة <strong>(${serviceName})</strong> بنجاح.<br>
          سيقوم المهندس <strong>أبو حيدر</strong> بالتواصل معك فوراً لتأكيد الموعد وتفاصيل التشخيص.
        </p>
        <button class="btn btn-primary modal-close-trigger" style="width: 100%;">ممتاز، شكراً لك</button>
      </div>
    `;
    document.body.appendChild(successModal);

    const closeBtn = successModal.querySelector('.modal-close-trigger');
    closeBtn.addEventListener('click', () => {
      successModal.classList.remove('active');
      setTimeout(() => successModal.remove(), 300);
    });
  }

  // Booking Form Submission
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('clientName')?.value || 'عميلنا العزيز';
      const service = document.getElementById('requiredService')?.value || 'صيانة عامة';
      
      showSuccessModal(name, service);
      bookingForm.reset();
    });
  }

  // Contact Form Submission
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName')?.value || 'عميلنا العزيز';
      
      showSuccessModal(name, 'استفسار عام');
      contactForm.reset();
    });
  }
});
