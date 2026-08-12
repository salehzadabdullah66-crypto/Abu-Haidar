# -*- coding: utf-8 -*-
"""
Abu Haider Maintenance - Social Media Links Updater
"""

import os
import re

INSTAGRAM_URL = "https://www.instagram.com/ab0_h96?igsh=dmVxazNldXY3MWMx"
TIKTOK_URL = "https://www.tiktok.com/@abohaydar013?_r=1&_t=ZS-98pf8tB8qc1"

directories = [
    r"c:\Users\PC\Desktop\ابو حيدر خاص",
    r"c:\Users\PC\Desktop\ابو حيدر خاص\tr"
]

for d in directories:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if f.endswith('.html'):
            path = os.path.join(d, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace instagram link placeholder
            content = re.sub(
                r'<a\s+href="[^"]*"\s+class="social-link">\s*<i\s+class="fab\s+fa-instagram">\s*</i>\s*</a>',
                f'<a href="{INSTAGRAM_URL}" target="_blank" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>',
                content
            )

            # Replace tiktok link placeholder
            content = re.sub(
                r'<a\s+href="[^"]*"\s+class="social-link">\s*<i\s+class="fab\s+fa-tiktok">\s*</i>\s*</a>',
                f'<a href="{TIKTOK_URL}" target="_blank" class="social-link" title="TikTok"><i class="fab fa-tiktok"></i></a>',
                content
            )

            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated social links in {f}")

print("All social media links updated successfully!")
