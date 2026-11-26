with open('emergent_main.js', 'r', encoding='utf-8') as f:
    s = f.read()

idx = s.find('hemisphereLight')
# Search backwards 15000 chars and forwards 5000 chars
chunk = s[max(0, idx - 12000) : idx + 2000]

with open('emergent_components_decompiled.js', 'w', encoding='utf-8') as out:
    out.write(chunk)
print('Wrote emergent_components_decompiled.js, length:', len(chunk))
