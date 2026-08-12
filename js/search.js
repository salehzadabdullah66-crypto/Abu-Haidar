/**
 * Abu Haider Maintenance - Live Instant Search Modal Engine
 */
document.addEventListener('DOMContentLoaded', () => {
  const searchTriggerBtns = document.querySelectorAll('.search-trigger');
  
  // Build Search Modal DOM Element
  const searchModalOverlay = document.createElement('div');
  searchModalOverlay.className = 'modal-overlay search-modal-overlay';
  searchModalOverlay.innerHTML = `
    <div class="modal-content search-modal-box">
      <button class="modal-close-btn search-modal-close"><i class="fas fa-times"></i></button>
      <h3 style="margin-bottom: 1.2rem; color: var(--color-gold); font-size: 1.3rem;">
        <i class="fas fa-search"></i> ابحث عن خدمة أو عطل لجهازك
      </h3>
      <div class="search-input-wrapper">
        <i class="fas fa-search"></i>
        <input type="text" class="form-control search-field" placeholder="مثال: تبديل بطارية، شاشة مكسورة، تسريع لابتوب، آيفون..." />
      </div>
      <div class="search-results-list"></div>
    </div>
  `;
  document.body.appendChild(searchModalOverlay);

  const searchField = searchModalOverlay.querySelector('.search-field');
  const searchResultsList = searchModalOverlay.querySelector('.search-results-list');
  const searchCloseBtn = searchModalOverlay.querySelector('.search-modal-close');

  const servicesData = [
    { title: "صيانة الهواتف الذكية", url: "phones.html", desc: "إصلاح جميع أعطال الآيفون، سامسونج، شاومي، وأوبو", category: "هواتف" },
    { title: "تبديل الشاشات المكسورة", url: "phones.html", desc: "تغيير شاشات أصلي OLED & AMOLED بضمان", category: "شاشات" },
    { title: "تبديل البطارية والتغذية", url: "phones.html", desc: "حل مشكلة التفريغ السريع والانتفاخ ببطاريات ممتازة", category: "بطاريات" },
    { title: "صيانة الكمبيوتر واللابتوب", url: "computers.html", desc: "تشخيص وإصلاح كافة أعطال الأجهزة المكتبية والمحمولة", category: "كمبيوتر" },
    { title: "تركيب SSD وتوسيع RAM", url: "computers.html", desc: "تسريع اللابتوب والكمبيوتر حتى 5 أضعاف", category: "تسريع" },
    { title: "تغيير المعجون الحراري وتنظيف الجهاز", url: "computers.html", desc: "حل مشكلة الحرارة وصوت المروحة العالي", category: "حرارة" },
    { title: "إزالة الفيروسات وحل مشاكل Windows", url: "computers.html", desc: "فورمات احترافي مع تثبيت التعريفات والبرامج الأصلية", category: "برمجيات" },
    { title: "استعادة الملفات والبيانات", url: "services.html", desc: "محاولة استرجاع الصور والملفات من الأجهزة المتضررة", category: "بيانات" },
    { title: "احجز موعد صيانة", url: "repairs.html", desc: "حجز موعد تشخيص سريع في ورشة أبو حيدر", category: "حجز" }
  ];

  function openSearchModal() {
    searchModalOverlay.classList.add('active');
    setTimeout(() => searchField?.focus(), 150);
  }

  function closeSearchModal() {
    searchModalOverlay.classList.remove('active');
  }

  searchTriggerBtns.forEach(btn => btn.addEventListener('click', openSearchModal));
  searchCloseBtn?.addEventListener('click', closeSearchModal);

  searchModalOverlay.addEventListener('click', (e) => {
    if (e.target === searchModalOverlay) closeSearchModal();
  });

  searchField?.addEventListener('input', (e) => {
    const query = e.target.value.trim().toLowerCase();
    if (!query) {
      searchResultsList.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 1.5rem;">اكتب شيئاً للبحث عن الخدمات والأعطال...</p>';
      return;
    }

    const filtered = servicesData.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.desc.toLowerCase().includes(query) ||
      item.category.toLowerCase().includes(query)
    );

    if (filtered.length === 0) {
      searchResultsList.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 1.5rem;">لم نجد نتائج مطابقة، يمكنك التواصل مباشرة مع أبو حيدر للإستفسار.</p>';
    } else {
      searchResultsList.innerHTML = filtered.map(item => `
        <a href="${item.url}" class="search-result-item">
          <div>
            <h4 style="font-weight: 800; color: var(--text-main);">${item.title}</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">${item.desc}</p>
          </div>
          <span style="background: rgba(255, 215, 0, 0.1); color: var(--color-gold); font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 6px;">${item.category}</span>
        </a>
      `).join('');
    }
  });
});
