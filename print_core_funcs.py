with open('emergent_core_scene.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect functions in this chunk
import re
print("Functions in core scene:")
for m in re.finditer(r'function\s+([A-Za-z0-9_]+)\s*\([^)]*\)\s*\{', text):
    start = m.start()
    name = m.group(1)
    print(f'=== FUNCTION {name} ===')
    print(text[start : start + 600])
    print('-----------------------------------------')
