import subprocess, time, json, urllib.request, base64
from websocket import create_connection

def run():
    target_url = 'https://0262ab0a-85f6-468a-9037-aff82d6b7f14-00-npv5e28o8k2f.pike.replit.dev/'
    print(f'Starting Chrome to inspect {target_url}...')
    proc = subprocess.Popen([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new',
        '--remote-debugging-port=9222',
        '--remote-allow-origins=*',
        '--window-size=1440,900',
        target_url
    ])
    time.sleep(5)

    try:
        resp = urllib.request.urlopen('http://localhost:9222/json')
        pages = json.loads(resp.read().decode())
        ws_url = None
        for p in pages:
            if 'replit.dev' in p.get('url', ''):
                ws_url = p.get('webSocketDebuggerUrl')
                break

        if not ws_url and pages:
            ws_url = pages[0].get('webSocketDebuggerUrl')

        if not ws_url:
            print('Could not find page WS URL')
            return

        ws = create_connection(ws_url)
        msg_id = 1

        def send_cmd(method, params=None):
            nonlocal msg_id
            cmd = {'id': msg_id, 'method': method}
            if params:
                cmd['params'] = params
            ws.send(json.dumps(cmd))
            msg_id += 1
            while True:
                res = json.loads(ws.recv())
                if res.get('id') == cmd['id']:
                    return res

        send_cmd('Page.enable')
        # Wait for potential redirect or verification
        time.sleep(4)

        # Capture screenshot
        res = send_cmd('Page.captureScreenshot', {'format': 'png'})
        data = res['result']['data']
        with open(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\replit_reference_screenshot.png', 'wb') as f:
            f.write(base64.b64decode(data))
        print('Captured replit_reference_screenshot.png')

        # Get DOM title and innerText
        dom_res = send_cmd('Runtime.evaluate', {
            'expression': 'JSON.stringify({ title: document.title, url: window.location.href, text: document.body.innerText.slice(0, 4000) })'
        })
        info = json.loads(dom_res.get('result', {}).get('value', '{}'))
        print('PAGE INFO:', info.get('title'), info.get('url'))
        with open(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\replit_reference_text.txt', 'w', encoding='utf-8') as f:
            f.write(info.get('text', ''))

        ws.close()
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
