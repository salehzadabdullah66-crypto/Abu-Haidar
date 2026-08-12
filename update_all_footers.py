# -*- coding: utf-8 -*-
"""
Update footer socials across all HTML pages (Arabic & Turkish)
"""

import os
import re

INSTAGRAM_URL = "https://www.instagram.com/ab0_h96?igsh=dmVxazNldXY3MWMx"
TIKTOK_URL = "https://www.tiktok.com/@abohaydar013?_r=1&_t=ZS-98pf8tB8qc1"

new_socials = f'''<div class="footer-socials">
            <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
            <a href="{INSTAGRAM_URL}" target="_blank" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" class="social-link whatsapp-link"><i class="fab fa-whatsapp"></i></a>
            <a href="{TIKTOK_URL}" target="_blank" class="social-link" title="TikTok"><i class="fab fa-tiktok"></i></a>
          </div>'''

directories = [
    r"c:\Users\PC\Desktop\ابو حيدر خاص",
    r"c:\Users\PC\Desktop\ابو حيدر خاص\tr"
]

pattern = re.compile(r'<div class="footer-socials">.*?</div>', re.DOTALL)

for d in directories:
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith('.html'):
                path = os.path.join(d, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                content = pattern.sub(new_socials, content)

                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated footer socials in {f}")

print("All footers updated successfully!")
