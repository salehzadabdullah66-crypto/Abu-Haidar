# -*- coding: utf-8 -*-
"""
Abu Haider Tech Maintenance Center
Professional Turkish Translation & Multi-language Generator
"""

import os
import re

TR_DIR = r"c:\Users\PC\Desktop\ابو حيدر خاص\tr"
os.makedirs(TR_DIR, exist_ok=True)

# Update Arabic pages header to include TR language switch button
AR_PAGES_DIR = r"c:\Users\PC\Desktop\ابو حيدر خاص"
ar_files = [f for f in os.listdir(AR_PAGES_DIR) if f.endswith(".html")]

for ar_file in ar_files:
    file_path = os.path.join(AR_PAGES_DIR, ar_file)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add TR button if not already present
    if 'title="Türkçe"' not in content:
        tr_btn_html = f'<a href="tr/{ar_file}" class="header-icon-btn lang-btn" title="Türkçe" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">TR</a>\n        <button class="header-icon-btn theme-toggle-btn"'
        content = content.replace('<button class="header-icon-btn theme-toggle-btn"', tr_btn_html, 1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Added TR language button to Arabic pages successfully!")

# Define professional Turkish HTML contents for all 11 pages
pages_tr = {}

# 1. TR index.html
pages_tr["index.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abu Haider Telefon ve Bilgisayar Tamir Merkezi | Tecrübe • Hız • Güven</title>
  <meta name="description" content="Akıllı telefonlar, bilgisayarlar ve laptoplar için profesyonel tamir ve bakım merkezi. Orijinal yedek parça ve hızlı arıza tespiti.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/home.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style>
    body { direction: ltr; text-align: left; }
    .nav-menu { direction: ltr; }
    .footer-links a i { transform: rotate(180deg); }
    .typewriter-cursor { margin-left: 4px; margin-right: 0; }
  </style>
</head>
<body>

  <!-- Preloader Screen -->
  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider Logo" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <!-- Header Navbar -->
  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider Logo">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link active">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../index.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn">
          <span></span><span></span><span></span>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div class="mobile-nav-overlay"></div>
  <div class="mobile-nav">
    <a href="index.html" class="nav-link active">Ana Sayfa</a>
    <a href="about.html" class="nav-link">Hakkımızda</a>
    <a href="services.html" class="nav-link">Hizmetlerimiz</a>
    <a href="phones.html" class="nav-link">Telefon Tamiri</a>
    <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
    <a href="gallery.html" class="nav-link">Galeri</a>
    <a href="offers.html" class="nav-link">Fırsatlar</a>
    <a href="testimonials.html" class="nav-link">Yorumlar</a>
    <a href="faq.html" class="nav-link">SSS</a>
    <a href="contact.html" class="nav-link">İletişim</a>
    <a href="repairs.html" class="btn btn-primary" style="margin-top: 1rem;">Hemen Randevu Al</a>
  </div>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="container hero-grid">
      <div class="hero-content">
        
        <!-- Royal Frame Premium Typewriter Brand Element -->
        <div class="royal-frame-wrapper reveal">
          <div class="royal-frame">
            <div class="royal-frame-shine"></div>
            <div class="typewriter-box">
              <span class="typewriter-text" data-text="Abu Haider Cihaz ve Bilgisayar Tamiri"></span>
              <span class="typewriter-cursor"></span>
            </div>
          </div>
        </div>

        <h1 class="hero-main-title reveal">
          Abu Haider <span>Telefon & Bilgisayar Tamiri</span>
        </h1>
        <p class="hero-lead reveal">
          Cihazınızın performansını geri kazandırıyoruz... Size huzur veriyoruz. Hassas mikro lehimleme teknolojisi, orijinal yedek parça ve uzman işçilik.
        </p>

        <div class="hero-buttons reveal">
          <a href="repairs.html" class="btn btn-primary">
            <i class="fas fa-wrench"></i> Hemen Randevu Al
          </a>
          <a href="contact.html" class="btn btn-secondary">
            <i class="fas fa-headset"></i> İletişime Geç
          </a>
          <a href="#" class="btn btn-whatsapp whatsapp-link">
            <i class="fab fa-whatsapp"></i> Direkt WhatsApp
          </a>
        </div>
      </div>

      <div class="hero-visual reveal-left">
        <div class="hero-img-wrapper">
          <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider Tamir Merkezi">
          <div class="hero-badge-float">
            <i class="fas fa-shield-halved"></i>
            <div class="hero-badge-text">
              <h4>%100 Gerçek Garanti</h4>
              <p>Orijinal Parça ve Test Garantisi</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Quick Services Marquee Ticker -->
  <section class="ticker-section">
    <div class="ticker-track">
      <div class="ticker-item"><i class="fas fa-mobile-screen-button"></i> 📱 Akıllı Telefon Tamiri</div>
      <div class="ticker-item"><i class="fas fa-laptop-code"></i> 💻 Laptop & Bilgisayar Bakımı</div>
      <div class="ticker-item"><i class="fas fa-microchip"></i> 🔧 Anakart & Çip Onarımı</div>
      <div class="ticker-item"><i class="fas fa-battery-full"></i> 🔋 Orijinal Batarya Değişimi</div>
      <div class="ticker-item"><i class="fas fa-tv"></i> 🖥️ Ekran & Ekran Camı Değişimi</div>
      <div class="ticker-item"><i class="fas fa-hard-drive"></i> 💾 Veri Kurtarma Hizmetleri</div>
      <div class="ticker-item"><i class="fas fa-bolt"></i> ⚡ Hızlı & Hassas Arıza Tespiti</div>
      <div class="ticker-item"><i class="fas fa-screwdriver-wrench"></i> 🛠️ Profesyonel İşçilik</div>
    </div>
  </section>

  <!-- Services Section -->
  <section class="section-padding">
    <div class="container">
      <div class="section-header">
        <span class="section-subtitle"><i class="fas fa-cogs"></i> Hizmetlerimiz</span>
        <h2 class="section-title">Kapsamlı ve Uzman <span>Tamir Çözümleri</span></h2>
        <p class="section-description">Mikro lehimleme ve dijital mikroskop teknolojisi ile cihazlarınız için en güvenilir tamir çözümlerini sunuyoruz.</p>
      </div>

      <div class="cards-grid">
        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-mobile-alt"></i></div>
          <h3 class="service-title">Akıllı Telefon Tamiri</h3>
          <p class="service-text">iPhone, Samsung, Xiaomi, Oppo ve diğer tüm marka telefonlarınızın anakart ve donanım onarımı.</p>
          <a href="phones.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-battery-three-quarters"></i></div>
          <h3 class="service-title">Batarya Değişimi</h3>
          <p class="service-text">Eskimiş ve çabuk biten bataryalarınızı yüksek performanslı ve garantili bataryalarla değiştiriyoruz.</p>
          <a href="phones.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-desktop"></i></div>
          <h3 class="service-title">Ekran Onarımı & Değişimi</h3>
          <p class="service-text">Kırık ekranlarınızı yüksek kaliteli AMOLED ve OLED ekranlarla orijinal standartlarda değiştiriyoruz.</p>
          <a href="phones.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-laptop"></i></div>
          <h3 class="service-title">Bilgisayar & Laptop Bakımı</h3>
          <p class="service-text">Isınma, yavaşlama, mavi ekran ve anakart arızaları için garantili teknik servis çözümleri.</p>
          <a href="computers.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-database"></i></div>
          <h3 class="service-title">Veri Kurtarma</h3>
          <p class="service-text">Hasar görmüş veya sıvı teması almış cihazlarınızdan fotoğraf ve önemli dosyalarınızı kurtarıyoruz.</p>
          <a href="services.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-shield-virus"></i></div>
          <h3 class="service-title">Virüs Temizleme & SSD Yükseltme</h3>
          <p class="service-text">Zararlı yazılımların temizlenmesi, SSD ve RAM yükseltmesi ile bilgisayarınızı 5 kat hızlandırın.</p>
          <a href="computers.html" class="service-link">Detayları Gör <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </section>

  <!-- Why Choose Us Section -->
  <section class="section-padding" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header">
        <span class="section-subtitle"><i class="fas fa-star"></i> Neden Biz?</span>
        <h2 class="section-title">Neden <span>Abu Haider Tamir Merkezi?</span></h2>
        <p class="section-description">Cihazınızı fabrikasyon kalitesinde teslim etmek için dürüstlük ve şeffaflıkla çalışıyoruz.</p>
      </div>

      <div class="why-us-grid">
        <div class="why-card reveal">
          <div class="why-icon"><i class="fas fa-user-gear"></i></div>
          <h3 class="why-title">Köklü Teknik Tecrübe</h3>
          <p class="why-desc">Hassas mikro bileşenlerin onarımında uzun yıllara dayanan uzmanlık ve tecrübe.</p>
        </div>

        <div class="why-card reveal">
          <div class="why-icon"><i class="fas fa-microscope"></i></div>
          <h3 class="why-title">Hassas Arıza Tespiti</h3>
          <p class="why-desc">Dijital mikroskop ve modern test cihazlarıyla arızanın kaynağını doğru tespit ediyoruz.</p>
        </div>

        <div class="why-card reveal">
          <div class="why-icon"><i class="fas fa-gauge-high"></i></div>
          <h3 class="why-title">Hızlı Teslimat</h3>
          <p class="why-desc">Zamanınızın değerli olduğunu biliyoruz. Çoğu arızayı aynı gün içinde tamir ediyoruz.</p>
        </div>

        <div class="why-card reveal">
          <div class="why-icon"><i class="fas fa-certificate"></i></div>
          <h3 class="why-title">Kaliteli Parça & Garanti</h3>
          <p class="why-desc">Yapılan tüm işlemler ve değiştirilen parçalar için gerçek garanti sunuyoruz.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Owner Abu Haider Showcase Section -->
  <section class="section-padding owner-section">
    <div class="container owner-grid">
      <div class="owner-img-box reveal-right">
        <img src="../img/owner/abu-haider-owner.jpg" alt="Mühendis Abu Haider">
        <div class="owner-badge">
          <i class="fas fa-crown"></i> Mühendis Abu Haider
        </div>
      </div>

      <div class="owner-content reveal-left">
        <span class="section-subtitle"><i class="fas fa-award"></i> Merkez Yönetimi</span>
        <h2 class="section-title">Tanışın: <span>Mühendis Abu Haider</span></h2>
        <p style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
          Akıllı cihazlar ve bilgisayar teknolojisindeki uzun tecrübesiyle Mühendis <strong>Abu Haider</strong>, müşterilerine dürüst, şeffaf ve en yüksek kalitede teknik servis sunmak için bu merkezi kurmuştur.
        </p>
        <p style="font-size: 1.05rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 2rem;">
          "Amacımız sadece cihazınızı tamir etmek değil; dürüstlük, kalite ve zamanında teslimat ile aramızda kalıcı bir güven bağı kurmaktır."
        </p>

        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
          <a href="about.html" class="btn btn-primary"><i class="fas fa-user-circle"></i> Hikayemizi Oku</a>
          <a href="#" class="btn btn-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> Abu Haider ile Görüş</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo" style="margin-bottom: 1rem;">
            <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider Logo">
            <div class="brand-info">
              <span class="brand-title">Abu Haider</span>
              <span class="brand-tagline">Tecrübe • Hız • Güven</span>
            </div>
          </a>
          <p>Telefon ve bilgisayar tamirinde modern mikrolehimleme ekipmanları ile lider teknik servis merkezi.</p>
          <div class="footer-socials">
            <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
            <a href="#" class="social-link whatsapp-link"><i class="fab fa-whatsapp"></i></a>
            <a href="#" class="social-link"><i class="fab fa-tiktok"></i></a>
          </div>
        </div>

        <div class="footer-column">
          <h3>Hızlı Bağlantılar</h3>
          <div class="footer-links">
            <a href="index.html"><i class="fas fa-angle-right"></i> Ana Sayfa</a>
            <a href="about.html"><i class="fas fa-angle-right"></i> Hakkımızda</a>
            <a href="services.html"><i class="fas fa-angle-right"></i> Hizmetlerimiz</a>
            <a href="gallery.html"><i class="fas fa-angle-right"></i> Galeri</a>
            <a href="offers.html"><i class="fas fa-angle-right"></i> Kampanyalar</a>
          </div>
        </div>

        <div class="footer-column">
          <h3>Tamir Hizmetleri</h3>
          <div class="footer-links">
            <a href="phones.html"><i class="fas fa-angle-right"></i> iPhone Tamiri</a>
            <a href="phones.html"><i class="fas fa-angle-right"></i> Samsung Tamiri</a>
            <a href="computers.html"><i class="fas fa-angle-right"></i> Laptop Hızlandırma</a>
            <a href="computers.html"><i class="fas fa-angle-right"></i> Format & Windows</a>
            <a href="repairs.html"><i class="fas fa-angle-right"></i> Randevu Al</a>
          </div>
        </div>

        <div class="footer-column">
          <h3>İletişim</h3>
          <a href="https://maps.app.goo.gl/euoS5bxRguUMzP6A6" target="_blank" class="footer-contact-item">
            <i class="fas fa-location-dot"></i>
            <span>Merkez Şube (Haritada Açmak İçin Tıklayın)</span>
          </a>
          <div class="footer-contact-item">
            <i class="fas fa-phone"></i>
            <span>Telefon / WhatsApp: +90 539 911 8999</span>
          </div>
          <div class="footer-contact-item">
            <i class="fas fa-clock"></i>
            <span>Çalışma Saatleri: Her gün 09:00 - 22:00</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link" title="WhatsApp ile İletişim">
    <i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span>
  </a>
  <button class="back-to-top" title="Yukarı Çık"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/slider.js"></script>
  <script src="../js/filter.js"></script>
  <script src="../js/gallery.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/contact.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 2. TR about.html
pages_tr["about.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hakkımızda | Abu Haider Tamir Merkezi</title>
  <meta name="description" content="Abu Haider teknik servisinin kuruluş hikayesi, tecrübesi ve kalite vizyonu.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/home.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link active">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../about.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-info-circle"></i> Teknik Servisimiz</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Abu Haider <span>Hikayesi & Vizyonu</span></h1>
      <p class="section-description">Teknoloji dünyasında güvenilir ve üst düzey tamir hizmetleri sunuyoruz.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container owner-grid">
      <div class="owner-img-box reveal-right">
        <img src="../img/owner/abu-haider-owner.jpg" alt="Abu Haider">
        <div class="owner-badge">
          <i class="fas fa-certificate"></i> Mühendis Abu Haider
        </div>
      </div>

      <div class="owner-content reveal-left">
        <span class="section-subtitle"><i class="fas fa-handshake"></i> Kalite ve Güven</span>
        <h2 class="section-title">Temel İlkemiz: <span>Kalite ve Müşteri Memnuniyeti</span></h2>
        <p style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem;">
          <strong>Abu Haider Tamir Merkezi</strong>, elektronik cihazlara olan tutku ve hassasiyetle kuruldu. Yüzeysel tamirler yerine dijital mikroskoplar ve modern ölçüm cihazları ile anakart üzerindeki hassas mikro arızaları başarıyla gideriyoruz.
        </p>
        
        <div class="cards-grid" style="grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem;">
          <div style="background: var(--bg-card); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-glass);">
            <h4 style="color: var(--color-gold); font-size: 1.2rem; font-weight: 800; margin-bottom: 0.5rem;"><i class="fas fa-bullseye"></i> Misyonumuz</h4>
            <p style="font-size: 0.9rem; color: var(--text-muted);">Cihazlarınızı en yüksek hızda tamir ederken kişisel verilerinizin gizliliğini tam güvence altında tutmak.</p>
          </div>
          <div style="background: var(--bg-card); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-glass);">
            <h4 style="color: var(--color-cyan); font-size: 1.2rem; font-weight: 800; margin-bottom: 0.5rem;"><i class="fas fa-eye"></i> Vizyonumuz</h4>
            <p style="font-size: 0.9rem; color: var(--text-muted);">Bölgenin en çok tercih edilen ve güven duyulan 1 numaralı teknik servis merkezi olmak.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 3. TR services.html
pages_tr["services.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tüm Hizmetlerimiz | Abu Haider</title>
  <meta name="description" content="Abu Haider teknik servisinde sunulan tüm profesyonel tamir hizmetleri.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link active">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../services.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-tools"></i> Hizmet Kataloğumuz</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Profesyonel <span>Teknik Servis Çözümleri</span></h1>
      <p class="section-description">Cihazınız için en uygun tamir seçeneğini belirleyin.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="cards-grid">
        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-mobile-screen"></i></div>
          <h3 class="service-title">📱 Akıllı Telefon Tamiri</h3>
          <p class="service-text">iPhone ve Android cihazların ekran, batarya, şarj soketi ve anakart arızalarının onarımı.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Telefon Tamiri İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-battery-charging"></i></div>
          <h3 class="service-title">🔋 Batarya Değişimi</h3>
          <p class="service-text">%100 Orijinal kaliteli bataryalar ile uzun pil ömrü ve garantili kullanım.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Batarya Değişimi İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-laptop-medical"></i></div>
          <h3 class="service-title">💻 Laptop & Bilgisayar Bakımı</h3>
          <p class="service-text">İşlemci ısınması, fan gürültüsü, mavi ekran ve şarj entegresi onarımı.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Laptop Bakımı İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-database"></i></div>
          <h3 class="service-title">💾 Veri Kurtarma</h3>
          <p class="service-text">Sıvı teması almış veya açılmayan cihazlardan resim ve dosyaların güvenli bir şekilde kurtarılması.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Veri Kurtarma İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-shield-virus"></i></div>
          <h3 class="service-title">🦠 Virüs Temizleme & Yazılım</h3>
          <p class="service-text">Zararlı yazılımların temizlenmesi, orijinal Windows kurulumu ve sürücü güncellemeleri.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Yazılım Destek İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-gauge-high"></i></div>
          <h3 class="service-title">⚡ Donanım Yükseltme</h3>
          <p class="service-text">SSD takılması ve RAM yükseltilmesi ile bilgisayar performansının katlanması.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">SSD Yükseltme İste</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 4. TR phones.html
pages_tr["phones.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Akıllı Telefon Tamiri | Abu Haider</title>
  <meta name="description" content="iPhone, Samsung, Xiaomi, Oppo ve Huawei telefonların garantili tamir hizmeti.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link active">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../phones.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-mobile"></i> Mobil Cihaz Departmanı</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Tüm Markalarda <span>Uzman Telefon Tamiri</span></h1>
      <p class="section-description">iPhone, Samsung, Xiaomi, Oppo ve Huawei serilerinde garantili mikrolehimleme çözümleri.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="cards-grid">
        <div class="device-card reveal">
          <div class="device-card-header">
            <i class="fab fa-apple"></i>
            <div>
              <h3 style="font-weight: 800;">iPhone Tamiri</h3>
              <span style="font-size: 0.85rem; color: var(--text-muted);">iPhone 11 - 15 Pro Max Serileri</span>
            </div>
          </div>
          <div class="device-card-body">
            <div class="device-issues-list">
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> TrueTone Destekli Orijinal Ekran Değişimi</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> %100 Pil Sağlığı Destekli Batarya Değişimi</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Şarj Entegresi ve Anakart Kasa Onarımı</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Lazerle Arka Cam Onarımı</div>
            </div>
            <a href="repairs.html" class="btn btn-primary" style="width: 100%; margin-top: 1.5rem; font-size: 0.9rem;">iPhone Randevusu Al</a>
          </div>
        </div>

        <div class="device-card reveal">
          <div class="device-card-header">
            <i class="fas fa-mobile-retro" style="color: #00e5ff;"></i>
            <div>
              <h3 style="font-weight: 800;">Samsung Tamiri</h3>
              <span style="font-size: 0.85rem; color: var(--text-muted);">Galaxy S, Note, A & Z Fold/Flip</span>
            </div>
          </div>
          <div class="device-card-body">
            <div class="device-issues-list">
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Orijinal Dynamic AMOLED Ekran Değişimi</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Sürekli Yeniden Başlama Arızası Çözümü</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Type-C Hızlı Şarj Soketi Tamiri</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Parmak İzi ve Kamera Değişimi</div>
            </div>
            <a href="repairs.html" class="btn btn-primary" style="width: 100%; margin-top: 1.5rem; font-size: 0.9rem;">Samsung Randevusu Al</a>
          </div>
        </div>

        <div class="device-card reveal">
          <div class="device-card-header">
            <i class="fas fa-mobile" style="color: #ff6900;"></i>
            <div>
              <h3 style="font-weight: 800;">Xiaomi & Poco Tamiri</h3>
              <span style="font-size: 0.85rem; color: var(--text-muted);">Tüm Amiral Gemisi ve Fiyat/Performans Modelleri</span>
            </div>
          </div>
          <div class="device-card-body">
            <div class="device-issues-list">
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Anakart Aşırı Isınma Onarımı</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Yüksek Çözünürlüklü Ön Cam Değişimi</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Şebeke ve Mikrofon Sorunu Onarımı</div>
              <div class="device-issue-item"><i class="fas fa-check-circle"></i> Mi Account ve Yazılım Çökmesi Tamiri</div>
            </div>
            <a href="repairs.html" class="btn btn-primary" style="width: 100%; margin-top: 1.5rem; font-size: 0.9rem;">Xiaomi Randevusu Al</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 5. TR computers.html
pages_tr["computers.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bilgisayar & Laptop Tamiri | Abu Haider</title>
  <meta name="description" content="Laptop hızlandırma, termal macun yenileme, SSD & RAM yükseltme ve anakart tamiri.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link active">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../computers.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-laptop-code"></i> Masaüstü & Laptop Bakımı</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Profesyonel <span>Bilgisayar Servisi</span></h1>
      <p class="section-description">Masaüstü ve dizüstü bilgisayarlarınız için en yüksek hız ve kararlılık.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="cards-grid">
        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-microchip"></i></div>
          <h3 class="service-title">Hızlı NVMe SSD Montajı</h3>
          <p class="service-text">Eski HDD yerine yüksek hızlı NVMe SSD takılması. Bilgisayarınız 5 saniyede açılsın.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">SSD Randevusu Al</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-fan"></i></div>
          <h3 class="service-title">Termal Temizlik & Macun</h3>
          <p class="service-text">Fan toz temizliği ve yüksek iletkenlikli termal macun sürümü ile ısınma sorununa son.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Termal Bakım İste</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fab fa-windows"></i></div>
          <h3 class="service-title">Windows Kurulumu & Format</h3>
          <p class="service-text">Orijinal Windows 11 / 10 kurulumu, tüm sürücü ve güncellemelerin eksiksiz yüklenmesi.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">Format Randevusu Al</a>
        </div>

        <div class="service-card reveal">
          <div class="service-icon-wrapper"><i class="fas fa-memory"></i></div>
          <h3 class="service-title">RAM Bellek Yükseltme</h3>
          <p class="service-text">Tasarım ve oyun programları için yüksek frekanslı RAM takılması.</p>
          <a href="repairs.html" class="btn btn-primary" style="font-size: 0.85rem; padding: 0.6rem 1.2rem;">RAM Yükseltme İste</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 6. TR repairs.html
pages_tr["repairs.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tamir Randevusu Al | Abu Haider</title>
  <meta name="description" content="Abu Haider teknik servisinde hızlı tamir ve arıza tespiti için online randevu formu.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../repairs.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-calendar-check"></i> Onaylı Servis Randevusu</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Abu Haider ile <span>Randevu Oluştur</span></h1>
      <p class="section-description">Cihaz bilgilerinizi doldurun, teknisyenimiz hemen sizinle iletişime geçsin.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container" style="max-width: 850px;">
      <div class="form-card reveal">
        <form id="bookingForm">
          <div class="form-grid">
            <div class="form-group">
              <label class="form-label" for="clientName"><i class="fas fa-user"></i> Adınız Soyadınız *</label>
              <input type="text" id="clientName" class="form-control" placeholder="Adınızı yazın" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="clientPhone"><i class="fas fa-phone"></i> Telefon / WhatsApp *</label>
              <input type="tel" id="clientPhone" class="form-control" placeholder="+90 5XX XXX XX XX" required>
            </div>
          </div>

          <div class="form-grid">
            <div class="form-group">
              <label class="form-label" for="deviceType"><i class="fas fa-laptop-mobile"></i> Cihaz Türü *</label>
              <select id="deviceType" class="form-control" required>
                <option value="" disabled selected>Cihaz Türü Seçin</option>
                <option value="Akıllı Telefon">Akıllı Telefon</option>
                <option value="Dizüstü Bilgisayar (Laptop)">Dizüstü Bilgisayar (Laptop)</option>
                <option value="Masaüstü PC">Masaüstü PC</option>
                <option value="Tablet / iPad">Tablet / iPad</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label" for="deviceBrand"><i class="fas fa-tag"></i> Marka & Model</label>
              <input type="text" id="deviceBrand" class="form-control" placeholder="Örn: iPhone 14 Pro / HP Laptop">
            </div>
          </div>

          <div class="form-group">
            <label class="form-label" for="deviceProblem"><i class="fas fa-comment-dots"></i> Arıza Açıklaması</label>
            <textarea id="deviceProblem" class="form-control" placeholder="Cihazdaki sorunu kısaca açıklayın..."></textarea>
          </div>

          <button type="submit" class="btn btn-primary" style="width: 100%; padding: 1.1rem; font-size: 1.1rem; margin-top: 1rem;">
            <i class="fas fa-paper-plane"></i> Servis Randevusunu Gönder
          </button>
        </form>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/contact.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 7. TR gallery.html
pages_tr["gallery.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galeri | Abu Haider</title>
  <meta name="description" content="Abu Haider teknik servis atölyesinden fotoğraf ve tamamlanan tamir çalışmaları.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style>
    body { direction: ltr; text-align: left; }
    .filter-bar { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 3rem; }
    .filter-btn { padding: 0.6rem 1.4rem; border-radius: 999px; background: var(--bg-tertiary); border: 1px solid var(--border-glass); color: var(--text-main); font-weight: 700; cursor: pointer; }
    .filter-btn.active { background: var(--color-gold); color: #000; }
    .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
    .gallery-item { position: relative; border-radius: 16px; overflow: hidden; border: 1px solid var(--border-glass); background: var(--bg-card); }
    .gallery-item img { width: 100%; height: 240px; object-fit: cover; }
    .gallery-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.7); backdrop-filter: blur(4px); display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s; padding: 1.5rem; text-align: center; }
    .gallery-item:hover .gallery-overlay { opacity: 1; }
  </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link active">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../gallery.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-images"></i> Çalışmalarımız</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Abu Haider <span>Tamir Galerisi</span></h1>
      <p class="section-description">Atölyemizden ve hassas mikrolehimleme çalışmalarımızdan kareler.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="filter-bar">
        <button class="filter-btn active" data-filter="all">Hepsini Göster</button>
        <button class="filter-btn" data-filter="phones">Telefon Tamiri</button>
        <button class="filter-btn" data-filter="computers">Bilgisayar Tamiri</button>
        <button class="filter-btn" data-filter="workshop">Atölye</button>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item" data-category="phones">
          <img src="../img/phones/phones-repair.png" alt="iPhone Anakart Tamiri">
          <div class="gallery-overlay">
            <h4 style="color: var(--color-gold); font-weight: 800;">iPhone Anakart Lehimleme</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">Dijital mikroskop altında hassas tamir</p>
            <a href="../img/phones/phones-repair.png" class="btn btn-primary gallery-zoom-btn" style="font-size: 0.8rem; padding: 0.4rem 1rem;"><i class="fas fa-search-plus"></i> Resmi Büyüt</a>
          </div>
        </div>

        <div class="gallery-item" data-category="computers">
          <img src="../img/computers/computers-repair.png" alt="Laptop Bakımı">
          <div class="gallery-overlay">
            <h4 style="color: var(--color-gold); font-weight: 800;">Laptop Fan & Termal Macun</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">Sıcaklık düşürme işlemi</p>
            <a href="../img/computers/computers-repair.png" class="btn btn-primary gallery-zoom-btn" style="font-size: 0.8rem; padding: 0.4rem 1rem;"><i class="fas fa-search-plus"></i> Resmi Büyüt</a>
          </div>
        </div>

        <div class="gallery-item" data-category="workshop">
          <img src="../img/repairs/workshop.png" alt="Atölye">
          <div class="gallery-overlay">
            <h4 style="color: var(--color-gold); font-weight: 800;">Modern Test Ekipmanları</h4>
            <p style="font-size: 0.85rem; color: var(--text-muted);">Abu Haider Teknik Laboratuvarı</p>
            <a href="../img/repairs/workshop.png" class="btn btn-primary gallery-zoom-btn" style="font-size: 0.8rem; padding: 0.4rem 1rem;"><i class="fas fa-search-plus"></i> Resmi Büyüt</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/filter.js"></script>
  <script src="../js/gallery.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 8. TR offers.html
pages_tr["offers.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kampanyalar | Abu Haider</title>
  <meta name="description" content="Abu Haider tamir merkezinde geçerli özel indirim ve bakım kampanyaları.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link active">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../offers.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-fire"></i> Sınırlı Süreli</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Abu Haider <span>Özel İndirimleri</span></h1>
      <p class="section-description">Ekran, batarya ve laptop bakımlarında geçerli indirimleri kaçırmayın.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="cards-grid">
        <div class="offer-card reveal">
          <span class="offer-badge">%25 İndirim 🔥</span>
          <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem;">Ekran Değişimi Paketi</h3>
          <p style="font-size: 0.92rem; color: var(--text-muted);">iPhone veya Samsung ekran değişiminde nano kırılmaz cam hediye.</p>
          <a href="repairs.html" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Kampanyadan Yararlan</a>
        </div>

        <div class="offer-card reveal">
          <span class="offer-badge">Özel Fırsat ⚡</span>
          <h3 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem;">Laptop Genel Bakım Paketi</h3>
          <p style="font-size: 0.92rem; color: var(--text-muted);">Fan temizliği + orijinal termal macun + ücretsiz format.</p>
          <a href="repairs.html" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Kampanyadan Yararlan</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 9. TR testimonials.html
pages_tr["testimonials.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Müşteri Yorumları | Abu Haider</title>
  <meta name="description" content="Abu Haider teknik servisi müşterilerinin deneyimleri ve değerlendirmeleri.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style>
    body { direction: ltr; text-align: left; }
    .slider-wrapper { position: relative; overflow: hidden; padding: 2rem 0; max-width: 850px; margin: 0 auto; }
    .testimonials-slider { display: flex; position: relative; min-height: 220px; }
    .testimonial-slide { min-width: 100%; opacity: 0; transition: opacity 0.5s; position: absolute; top:0; left:0; }
    .testimonial-slide.active { opacity: 1; position: relative; }
  </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link active">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../testimonials.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-comments"></i> Değerlendirmeler</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Müşterilerimiz <span>Ne Diyor?</span></h1>
      <p class="section-description">Teknik servisimizden hizmet alan müşterilerimizin gerçek yorumları.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="slider-wrapper">
        <div class="testimonials-slider">
          <div class="testimonial-slide active">
            <div class="testimonial-card">
              <div class="testimonial-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
              <p class="testimonial-quote">"Laptopum sürekli ısınıp kapanıyordu. Abu Haider ustam temizliğini yapıp macunu yeniledi. Bilgisayarım şimdi uçuyor, çok teşekkürler!"</p>
              <div class="testimonial-author">
                <div class="author-info">
                  <h4>Ahmet K.</h4>
                  <p>HP Laptop Tamiri</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/slider.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# 10. TR faq.html
pages_tr["faq.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sıkça Sorulan Sorular | Abu Haider</title>
  <meta name="description" content="Abu Haider tamir servisi hakkında merak edilen tüm sorular ve cevapları.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/cards.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style>
    body { direction: ltr; text-align: left; }
    .faq-container { max-width: 850px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.25rem; }
    .faq-item { background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 16px; overflow: hidden; }
    .faq-header { padding: 1.4rem 1.8rem; display: flex; align-items: center; justify-content: space-between; cursor: pointer; font-size: 1.15rem; font-weight: 800; }
    .faq-body { padding: 0 1.8rem 1.5rem 1.8rem; display: none; color: var(--text-muted); border-top: 1px dashed var(--border-glass); padding-top: 1rem; }
    .faq-item.active .faq-body { display: block; }
  </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link active">SSS</a>
        <a href="contact.html" class="nav-link">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../faq.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 4rem); padding-bottom: 4rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-circle-question"></i> SSS</span>
      <h1 class="section-title" style="font-size: 3rem; margin-top: 0.5rem;">Sıkça Sorulan <span>Sorular</span></h1>
      <p class="section-description">Teknik servisimiz hakkında en çok sorulan soruların cevapları.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="faq-container">
        <div class="faq-item active">
          <div class="faq-header">
            <span>Tamir işlemlerinde garanti veriyor musunuz?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-body">
            Evet! Değiştirilen yedek parçalar (ekran, batarya vb.) ve yapılan işçilikler için yazılı ve gerçek servis garantisi sunuyoruz.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-header">
            <span>Tamir süresi ortalama ne kadar sürer?</span>
            <i class="fas fa-chevron-down"></i>
          </div>
          <div class="faq-body">
            Ekran ve batarya değişimi gibi işlemler 1 - 2 saat içinde teslim edilir. Ağır anakart arızaları ise 24-48 saat sürebilir.
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/main.js"></script>
  <script>
    document.querySelectorAll('.faq-header').forEach(header => {
      header.addEventListener('click', () => {
        header.parentElement.classList.toggle('active');
      });
    });
  </script>
</body>
</html>
"""

# 11. TR contact.html
pages_tr["contact.html"] = """<!DOCTYPE html>
<html lang="tr" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>İletişim | Abu Haider</title>
  <meta name="description" content="Abu Haider teknik servis iletişim bilgileri, telefon, WhatsApp ve harita konumu.">
  <link rel="shortcut icon" href="../img/logo/abu-haider-logo.jpg" type="image/x-icon">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/header.css">
  <link rel="stylesheet" href="../css/footer.css">
  <link rel="stylesheet" href="../css/forms.css">
  <link rel="stylesheet" href="../css/animations.css">
  <link rel="stylesheet" href="../css/responsive.css">
  <style> body { direction: ltr; text-align: left; } </style>
</head>
<body>

  <div class="preloader">
    <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider" class="preloader-logo">
    <div class="preloader-spinner"></div>
  </div>

  <header class="header">
    <div class="container nav-container">
      <a href="index.html" class="brand-logo">
        <img src="../img/logo/abu-haider-logo.jpg" alt="Abu Haider">
        <div class="brand-info">
          <span class="brand-title">Abu Haider</span>
          <span class="brand-tagline">Tecrübe • Hız • Güven</span>
        </div>
      </a>

      <nav class="nav-menu">
        <a href="index.html" class="nav-link">Ana Sayfa</a>
        <a href="about.html" class="nav-link">Hakkımızda</a>
        <a href="services.html" class="nav-link">Hizmetlerimiz</a>
        <a href="phones.html" class="nav-link">Telefon Tamiri</a>
        <a href="computers.html" class="nav-link">Bilgisayar Tamiri</a>
        <a href="gallery.html" class="nav-link">Galeri</a>
        <a href="offers.html" class="nav-link">Fırsatlar</a>
        <a href="testimonials.html" class="nav-link">Yorumlar</a>
        <a href="faq.html" class="nav-link">SSS</a>
        <a href="contact.html" class="nav-link active">İletişim</a>
      </nav>

      <div class="header-actions">
        <a href="../contact.html" class="header-icon-btn lang-btn" title="العربية" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">AR</a>
        <button class="header-icon-btn theme-toggle-btn" title="Koyu/Açık Mod"><i class="fas fa-moon"></i></button>
        <button class="header-icon-btn search-trigger" title="Hızlı Arama"><i class="fas fa-search"></i></button>
        <a href="repairs.html" class="btn btn-primary" style="padding: 0.65rem 1.4rem; font-size: 0.9rem;">Randevu Al</a>
        <div class="hamburger-btn"><span></span><span></span><span></span></div>
      </div>
    </div>
  </header>

  <section style="padding-top: calc(var(--header-height) + 3rem); padding-bottom: 3.5rem; background: var(--bg-secondary); border-bottom: 1px solid var(--border-glass); text-align: center;">
    <div class="container">
      <span class="section-subtitle"><i class="fas fa-headset"></i> İletişim</span>
      <h1 class="section-title contact-hero-title" style="margin-top: 0.5rem;">Abu Haider ile <span>İletişime Geçin</span></h1>
      <p class="section-description">Sorularınız ve cihaz arıza kaydınız için bize ulaşın.</p>
    </div>
  </section>

  <section class="section-padding">
    <div class="container">
      <div class="contact-grid">
        
        <div>
          <h2 style="font-size: 1.8rem; font-weight: 800; color: var(--color-gold); margin-bottom: 1.5rem;">İletişim Bilgilerimiz</h2>
          
          <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 2.5rem;">
            <div class="contact-info-card">
              <div class="contact-info-card-icon" style="width: 50px; height: 50px; border-radius: 50%; background: rgba(255,215,0,0.1); color: var(--color-gold); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; flex-shrink: 0;">
                <i class="fas fa-phone-volume"></i>
              </div>
              <div>
                <h4 style="font-weight: 800;">Telefon / WhatsApp</h4>
                <p style="color: var(--text-muted); font-size: 0.95rem;">+90 539 911 8999</p>
              </div>
            </div>

            <div class="contact-info-card">
              <div class="contact-info-card-icon" style="width: 50px; height: 50px; border-radius: 50%; background: rgba(0,229,255,0.1); color: var(--color-cyan); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; flex-shrink: 0;">
                <i class="fas fa-location-dot"></i>
              </div>
              <div>
                <h4 style="font-weight: 800;">Merkez Konumu</h4>
                <a href="https://maps.app.goo.gl/euoS5bxRguUMzP6A6" target="_blank" style="color: var(--color-gold); font-weight: 700; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 0.4rem;">
                  <i class="fas fa-external-link-alt"></i> Google Maps Konumunu Aç
                </a>
              </div>
            </div>
          </div>

          <div class="contact-action-btns">
            <a href="tel:+905399118999" class="btn btn-primary"><i class="fas fa-phone"></i> Hemen Ara</a>
            <a href="#" class="btn btn-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> WhatsApp Mesajı</a>
            <a href="https://maps.app.goo.gl/euoS5bxRguUMzP6A6" target="_blank" class="btn btn-secondary"><i class="fas fa-map-location-dot"></i> Yol Tarifi Al</a>
          </div>
        </div>

        <div class="form-card">
          <h3 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 1.5rem;">Hızlı Mesaj Gönder</h3>
          <form id="contactForm">
            <div class="form-group">
              <label class="form-label" for="contactName"><i class="fas fa-user"></i> Adınız Soyadınız</label>
              <input type="text" id="contactName" class="form-control" placeholder="Adınızı girin" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="contactPhone"><i class="fas fa-phone"></i> Telefon Numarası</label>
              <input type="tel" id="contactPhone" class="form-control" placeholder="+90 5XX XXX XX XX" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="contactMsg"><i class="fas fa-envelope"></i> Mesajınız</label>
              <textarea id="contactMsg" class="form-control" placeholder="Mesajınızı buraya yazın..." required></textarea>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;"><i class="fas fa-paper-plane"></i> Mesajı Gönder</button>
          </form>
        </div>

      </div>

      <div class="contact-map-wrapper">
        <iframe class="contact-map-iframe" src="https://maps.google.com/maps?q=37.0710396,37.3945766&hl=tr&z=17&output=embed" allowfullscreen="" loading="lazy"></iframe>
        <a href="https://maps.app.goo.gl/euoS5bxRguUMzP6A6" target="_blank" class="btn btn-primary contact-map-btn" style="position: absolute; bottom: 15px; right: 15px; font-size: 0.85rem; padding: 0.65rem 1.2rem;">
          <i class="fas fa-map-location-dot"></i> Google Maps'te Aç
        </a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>© 2026 Abu Haider Telefon & Bilgisayar Tamir Merkezi — Tüm Hakları Saklıdır.</p>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-whatsapp whatsapp-link"><i class="fab fa-whatsapp"></i> <span>Abu Haider ile İletişim</span></a>
  <button class="back-to-top"><i class="fas fa-arrow-up"></i></button>

  <script src="../js/theme.js"></script>
  <script src="../js/menu.js"></script>
  <script src="../js/animation.js"></script>
  <script src="../js/search.js"></script>
  <script src="../js/contact.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

# Write all Turkish pages
for filename, code in pages_tr.items():
    file_path = os.path.join(TR_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Generated Turkish page: {filename}")

print("All 11 Turkish pages generated successfully!")
