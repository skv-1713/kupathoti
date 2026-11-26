import json, struct

with open('frontend/public/models/collection_vehicle.glb', 'rb') as f:
    f.seek(12)
    chunk_len, chunk_type = struct.unpack('<II', f.read(8))
    gltf = json.loads(f.read(chunk_len).decode('utf-8'))

for node in gltf['nodes']:
    if 'mesh' in node:
        m = gltf['meshes'][node['mesh']]
        for p in m['primitives']:
            mat_idx = p.get('material')
            mat_name = gltf['materials'][mat_idx]['name'] if mat_idx is not None else 'None'
            print(f"Node: {node.get('name')} -> Material: {mat_name}")
