# -*- coding: utf-8 -*-
"""
Apply complete 4-column footer with official Instagram and TikTok links to all Arabic & Turkish HTML pages.
"""

import os
import re

INSTAGRAM_URL = "https://www.instagram.com/ab0_h96?igsh=dmVxazNldXY3MWMx"
TIKTOK_URL = "https://www.tiktok.com/@abohaydar013?_r=1&_t=ZS-98pf8tB8qc1"

footer_ar = f'''<footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo" style="margin-bottom: 1rem;">
            <img src="img/logo/abu-haider-logo.jpg" alt="شعار أبو حيدر">
            <div class="brand-info">
              <span class="brand-title">أبو حيدر</span>
              <span class="brand-tagline">خبرة • سرعة • ثقة</span>
            </div>
          </a>
          <p>المركز المعتمد الأحدث لصيانة كافة الهواتف المحمولة والكمبيوترات، بأحدث معدات المايكروسولدر وشاشات وبطاريات عالية الجودة.</p>
          <div class="footer-socials">
            <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
            <a href="{INSTAGRAM_URL}" target="_blank" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" class="social-link whatsapp-link"><i class="fab fa-whatsapp"></i></a>
            <a href="{TIKTOK_URL}" target="_blank" class="social-link" title="TikTok"><i class="fab fa-tiktok"></i></a>
          </div>
        </div>

        <div class="footer-column">
          <h3>روابط سريعة</h3>
          <div class="footer-links">
            <a href="index.html"><i class="fas fa-angle-left"></i> الرئيسية</a>
            <a href="about.html"><i class="fas fa-angle-left"></i> من نحن</a>
            <a href="services.html"><i class="fas fa-angle-left"></i> الخدمات</a>
            <a href="gallery.html"><i class="fas fa-angle-left"></i> معرض الأعمال</a>
            <a href="offers.html"><i class="fas fa-angle-left"></i> العروض الحالية</a>
          </div>
        </div>

        <div class="footer-column">
          <h3>خدمات الصيانة</h3>
          <div class="footer-links">
            <a href="phones.html"><i class="fas fa-angle-left"></i> صيانة iPhone</a>
            <a href="phones.html"><i class="fas fa-angle-left"></i> صيانة Samsung</a>
            <a href="computers.html"><i class="fas fa-angle-left"></i> تسريع اللابتوبات</a>
            <a href="computers.html"><i class="fas fa-angle-left"></i> فورمات وWindows</a>
            <a href="repairs.html"><i class="fas fa-angle-left"></i> احجز موعد صيانة</a>
          </div>
        </div>

        <div class="footer-column">
          <h3>تواصل معنا</h3>
          <a href="https://maps.app.goo.gl/euoS5bxRguUMzP6A6" target="_blank" class="footer-contact-item">
            <i class="fas fa-location-dot"></i>
            <span>موقع الورشة الرئيسي (اضغط للفتح في الخريطة)</span>
          </a>
          <div class="footer-contact-item">
            <i class="fas fa-phone"></i>
            <span>هاتف / واتساب: +90 539 911 8999</span>
          </div>
          <div class="footer-contact-item">
            <i class="fas fa-clock"></i>
            <span>ساعات العمل: يومياً من 9:00 صباحاً حتى 10:00 مساءً</span>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 أبو حيدر لصيانة الهواتف والكمبيوترات — جميع الحقوق محفوظة.</p>
      </div>
    </div>
  </footer>'''

footer_tr = f'''<footer class="footer">
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
            <a href="{INSTAGRAM_URL}" target="_blank" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" class="social-link whatsapp-link"><i class="fab fa-whatsapp"></i></a>
            <a href="{TIKTOK_URL}" target="_blank" class="social-link" title="TikTok"><i class="fab fa-tiktok"></i></a>
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
  </footer>'''

pattern = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)

# Update Arabic pages
ar_dir = r"c:\Users\PC\Desktop\ابو حيدر خاص"
for f in os.listdir(ar_dir):
    if f.endswith('.html'):
        path = os.path.join(ar_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        content = pattern.sub(footer_ar, content)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated full footer in AR: {f}")

# Update Turkish pages
tr_dir = r"c:\Users\PC\Desktop\ابو حيدر خاص\tr"
for f in os.listdir(tr_dir):
    if f.endswith('.html'):
        path = os.path.join(tr_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        content = pattern.sub(footer_tr, content)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated full footer in TR: {f}")

print("All footers updated with full 4-column layout & social links!")
