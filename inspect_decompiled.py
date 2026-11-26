with open('emergent_components_decompiled.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for f_ =
import re
print("f_ definition:", re.findall(r'f_=\[[^\]]+\]', text))
print("g_ definition:", re.findall(r'g_=\{[^\}]+\}', text))
print("v_ definition:", re.findall(r'v_=\[[^\]]+\]', text))
print("y_ definition:", re.findall(r'y_=\[[^\]]+\]', text))

# Let's find definitions of F_, z_, N_, I_, etc.
for name in ['N_', 'I_', 'F_', 'z_', 'V_', 'j_', 'X_', 'q_']:
    m = re.search(r'function\s+' + name + r'\s*\([^)]*\)\s*\{', text)
    if m:
        start = m.start()
        print(f'=== Component {name} ===')
        print(text[start : start + 800])
        print('\n')
