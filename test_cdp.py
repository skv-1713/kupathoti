import subprocess, time, json, urllib.request, socket, os, base64

def get_websocket_url():
    resp = urllib.request.urlopen('http://localhost:9222/json')
    pages = json.loads(resp.read().decode())
    for p in pages:
        if 'localhost:5173' in p.get('url', ''):
            return p.get('webSocketDebuggerUrl')
    return None

print('Starting chrome...')
proc = subprocess.Popen([
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--remote-debugging-port=9222',
    '--disable-gpu',
    '--window-size=1440,900',
    'http://localhost:5173/'
])
time.sleep(3)

try:
    ws_url = get_websocket_url()
    print('WS URL:', ws_url)
finally:
    proc.terminate()
