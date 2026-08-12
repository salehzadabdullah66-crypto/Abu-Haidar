/**
 * Abu Haider Maintenance - Lightbox Modal Viewer
 */
document.addEventListener('DOMContentLoaded', () => {
  const lightboxOverlay = document.createElement('div');
  lightboxOverlay.className = 'modal-overlay lightbox-overlay';
  lightboxOverlay.innerHTML = `
    <div class="modal-content lightbox-content" style="max-width: 900px; padding: 1.5rem; text-align: center;">
      <button class="modal-close-btn lightbox-close"><i class="fas fa-times"></i></button>
      <img class="lightbox-img" src="" alt="Abu Haider Gallery Preview" style="width: 100%; max-height: 80vh; object-fit: contain; border-radius: 12px;" />
      <h3 class="lightbox-caption" style="margin-top: 1rem; color: var(--color-gold); font-size: 1.2rem;"></h3>
    </div>
  `;
  document.body.appendChild(lightboxOverlay);

  const lightboxImg = lightboxOverlay.querySelector('.lightbox-img');
  const lightboxCaption = lightboxOverlay.querySelector('.lightbox-caption');
  const lightboxClose = lightboxOverlay.querySelector('.lightbox-close');

  const galleryLinks = document.querySelectorAll('.gallery-zoom-btn');
  galleryLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const imgSrc = link.getAttribute('href') || link.getAttribute('data-src');
      const caption = link.getAttribute('data-caption') || 'صيانة أبو حيدر الاحترافية';
      
      if (imgSrc && lightboxImg) {
        lightboxImg.src = imgSrc;
        if (lightboxCaption) lightboxCaption.textContent = caption;
        lightboxOverlay.classList.add('active');
      }
    });
  });

  lightboxClose?.addEventListener('click', () => {
    lightboxOverlay.classList.remove('active');
  });

  lightboxOverlay.addEventListener('click', (e) => {
    if (e.target === lightboxOverlay) {
      lightboxOverlay.classList.remove('active');
    }
  });
});
