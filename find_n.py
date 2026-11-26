with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all occurrences of N_ = or function N_
import re
print("Matches for 'N_' :")
for m in re.finditer(r'[\s,;{(]([A-Za-z0-9_]*N_[A-Za-z0-9_]*)', text):
    start = m.start()
    print(text[start : start + 60])
