with open('emergent_extended.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find any assignment to f_, g_, v_, Q_, y_
for var in ['f_', 'g_', 'v_', 'Q_', 'y_', 'N_', 'I_', 'F_', 'z_', 'V_', 'j_', 'X_', 'q_']:
    matches = [m.start() for m in re.finditer(r'\b' + var + r'\b', text)]
    print(f'{var}: found {len(matches)} times')
    if matches:
        first = matches[0]
        print(f'  First match of {var} at {first}:')
        print('  ' + text[max(0, first - 40) : min(len(text), first + 120)])
