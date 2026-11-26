import json

with open(r'c:\Users\ELCOT\OneDrive\Desktop\kupathoti\frontend\public\models\smart_bin.glb', 'rb') as f:
    data = f.read()

# GLB header: magic (4 bytes), version (4 bytes), length (4 bytes)
# Chunk 0: length (4 bytes), type (4 bytes, 0x4E4F534A for JSON)
json_len = int.from_bytes(data[12:16], 'little')
json_bytes = data[20 : 20 + json_len]
gltf = json.loads(json_bytes.decode('utf-8'))

print('Nodes in smart_bin.glb:', len(gltf.get('nodes', [])))
for n in gltf.get('nodes', []):
    print('  Node:', n.get('name'))
