with open('emergent_env_F.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('treeCount')
if idx != -1:
    print('--- Tree code ---')
    print(text[idx - 50 : idx + 2000])
