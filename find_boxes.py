with open('emergent_env_F.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('boxGeometry')
while idx != -1:
    print('--- boxGeometry at', idx, '---')
    print(text[max(0, idx - 150) : min(len(text), idx + 250)])
    idx = text.find('boxGeometry', idx + 1)
