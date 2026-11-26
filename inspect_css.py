with open('emergent_main.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Search for hero styles
for cls in ['.hero', '.hero-title', '.hero-sub', '.hero-hint', '.nav', '.final', '.dot', '.f-mono']:
    idx = css.find(cls)
    if idx != -1:
        print(f'=== {cls} ===')
        print(css[idx : idx + 400])
        print('\n')
