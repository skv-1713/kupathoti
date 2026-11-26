with open('emergent_3d_scene.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('hemisphereLight')
print('Chars around hemisphereLight (from -300 to +300):')
print(repr(text[idx - 300 : idx + 300]))
