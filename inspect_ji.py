with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('function JI(')
if idx != -1:
    print('=== Component JI (Stage Cards) ===')
    print(text[idx : idx + 2500])

idx_h = text.find('h_=[')
if idx_h != -1:
    print('=== h_ array ===')
    print(text[idx_h : idx_h + 1200])
