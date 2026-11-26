with open('emergent_env_F.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('d.map(')
if idx != -1:
    print('Found d.map at:', idx)
    print(text[idx : idx + 1200])
else:
    # search for dodecahedron or icosahedron
    for geom in ['dodecahedron', 'icosahedron', 'cylinderGeometry', 'coneGeometry']:
        idx2 = text.find(geom)
        if idx2 != -1:
            print(f'Found {geom} at {idx2}:')
            print(text[idx2 - 100 : idx2 + 300])
