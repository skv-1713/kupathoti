with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find functions z_, F_, X_, q_, V_, j_
for name in ['z_', 'F_', 'X_', 'q_', 'V_', 'j_']:
    m = re.search(r'function\s+' + name + r'\s*\([^)]*\)\s*\{', text)
    if m:
        start = m.start()
        # Find closing brace or next function
        print(f'=== FUNCTION {name} ===')
        print(text[start : start + 2500])
        print('\n' + '='*50 + '\n')
