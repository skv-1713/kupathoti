with open('emergent_main.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('d_=')
if idx != -1:
    print('Found d_= at:', idx)
    print(text[max(0, idx - 500) : idx + 3000])

idx_bins = text.find('g_={')
if idx_bins != -1:
    print('\nFound g_={ at:', idx_bins)
    print(text[idx_bins : idx_bins + 2000])
