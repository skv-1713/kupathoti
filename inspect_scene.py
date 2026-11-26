with open('emergent_3d_scene.js', 'r', encoding='utf-8') as f:
    s = f.read()

# Let's search around hemisphereLight
idx = s.find('hemisphereLight')
if idx != -1:
    print('--- Code around hemisphereLight ---')
    print(s[idx - 500 : idx + 3500])
