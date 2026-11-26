with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function B_(')
if idx != -1:
    print('Found function B_ at:', idx)
    print(text[idx : idx + 1200])
