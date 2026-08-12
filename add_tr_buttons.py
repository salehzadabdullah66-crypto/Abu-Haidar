import os

ar_dir = r"c:\Users\PC\Desktop\ابو حيدر خاص"
for f in os.listdir(ar_dir):
    if f.endswith('.html'):
        path = os.path.join(ar_dir, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace header actions to include TR button and proper classes
        old_pattern = '<div class="header-actions">'
        new_pattern = f'<div class="header-actions">\n        <a href="tr/{f}" class="header-icon-btn lang-btn" title="Türkçe" style="font-weight: 800; font-size: 0.85rem; color: var(--color-gold);">TR</a>'
        
        if 'title="Türkçe"' not in content:
            content = content.replace(old_pattern, new_pattern, 1)
        
        content = content.replace('<button class="theme-toggle-btn"', '<button class="header-icon-btn theme-toggle-btn"')
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f} with TR language button!")
