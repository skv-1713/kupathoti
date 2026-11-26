with open('emergent_main.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.chapter')
if idx != -1:
    print('=== .chapter CSS ===')
    print(css[idx : idx + 1200])
