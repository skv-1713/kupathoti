with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Extract F_ (environment/buildings/trees/sidewalk)
m_F = re.search(r'function\s+F_\s*\([^)]*\)\s*\{', text)
if m_F:
    start = m_F.start()
    print('F_ length chunk:')
    chunk_F = text[start : start + 8000]
    with open('emergent_env_F.js', 'w', encoding='utf-8') as out:
        out.write(chunk_F)
    print('Wrote emergent_env_F.js')

# Extract z_ (bins)
m_z = re.search(r'function\s+z_\s*\([^)]*\)\s*\{', text)
if m_z:
    start = m_z.start()
    print('z_ length chunk:')
    chunk_z = text[start : start + 4000]
    with open('emergent_bin_z.js', 'w', encoding='utf-8') as out:
        out.write(chunk_z)
    print('Wrote emergent_bin_z.js')
