import subprocess, time, json, urllib.request, base64
from websocket import create_connection

def run():
    proc = subprocess.Popen([
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        '--headless=new',
        '--remote-debugging-port=9222',
        '--remote-allow-origins=*',
        '--disable-gpu',
        '--window-size=1440,900',
        'http://localhost:5173/citizen'
    ])
    time.sleep(3.5)

    try:
        resp = urllib.request.urlopen('http://localhost:9222/json')
        pages = json.loads(resp.read().decode())
        ws_url = None
        for p in pages:
            if 'localhost:5173' in p.get('url', ''):
                ws_url = p.get('webSocketDebuggerUrl')
                break

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

        def capture_screenshot(filename):
            res = send_cmd('Page.captureScreenshot', {'format': 'png'})
            data = res['result']['data']
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(data))
            print(f'Captured {filename}')

        send_cmd('Page.enable')
        time.sleep(2)

        # Click on the first report card (REQ-MAD-4201)
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const card = document.querySelector('div[class*="cursor-pointer"]');
                if (card) {
                    card.click();
                    console.log('Clicked card');
                }
            '''
        })
        time.sleep(1.5)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\citizen_tracker_modal_real.png')

        ws.close()
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
