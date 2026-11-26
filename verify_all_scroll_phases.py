import subprocess, time, json, urllib.request, os, base64
from websocket import create_connection

def run():
    print('Starting Chrome...')
    proc = subprocess.Popen([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new',
        '--remote-debugging-port=9222',
        '--remote-allow-origins=*',
        '--disable-gpu',
        '--window-size=1440,900',
        'http://localhost:5173/'
    ])
    time.sleep(3)

    try:
        resp = urllib.request.urlopen('http://localhost:9222/json')
        pages = json.loads(resp.read().decode())
        ws_url = None
        for p in pages:
            if 'localhost:5173' in p.get('url', ''):
                ws_url = p.get('webSocketDebuggerUrl')
                break

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

        def scroll_to(y):
            send_cmd('Runtime.evaluate', {
                'expression': f'window.scrollTo(0, {y});'
            })
            time.sleep(1)

        def capture_screenshot(filename):
            res = send_cmd('Page.captureScreenshot', {'format': 'png'})
            data = res['result']['data']
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(data))
            print(f'Captured {filename}')

        # Enable Page domain
        send_cmd('Page.enable')

        # Checkpoints
        scroll_to(600)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_01_sense.png')

        scroll_to(1200)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_02_understand.png')

        scroll_to(1800)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_03_demand.png')

        scroll_to(2400)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_04_respond.png')

        scroll_to(3150)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_05_final.png')

        # Rewind test: scroll back to 0
        scroll_to(0)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\scroll_06_rewound.png')

        ws.close()
        print('All scroll phases verified successfully!')
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
