with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('N_(){const e=Qe()')
if idx != -1:
    chunk = text[max(0, idx - 4000) : idx + 8000]
    with open('emergent_core_scene.js', 'w', encoding='utf-8') as out:
        out.write(chunk)
    print('Wrote emergent_core_scene.js, length:', len(chunk))
else:
    print('Not found!')
