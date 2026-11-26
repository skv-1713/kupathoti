import re

with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

assets = set(re.findall(r'\"([^\"]+\.(?:svg|png|jpg|jpeg|glb|gltf|woff2?))\"', text))
for a in assets:
    print(a)
