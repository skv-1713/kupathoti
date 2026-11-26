with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('hemisphereLight')
# Search backwards 50000 chars
chunk = text[max(0, idx - 40000) : idx + 5000]

with open('emergent_extended.js', 'w', encoding='utf-8') as out:
    out.write(chunk)

print('Wrote emergent_extended.js, length:', len(chunk))
matches = re.findall(r'(f_=[^;]+|g_=[^;]+|v_=[^;]+|y_=[^;]+|Q_=[^;]+)', chunk)
for m in matches[:10]:
    print('Match:', m[:150])
