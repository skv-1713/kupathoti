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

        # 1. Click "REPORT WASTE (+50 PTS)"
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const allButtons = Array.from(document.querySelectorAll('button'));
                const rep = allButtons.find(b => b.innerText && b.innerText.includes('REPORT WASTE'));
                if (rep) {
                    rep.click();
                    console.log('Clicked report button');
                } else {
                    console.log('Button not found');
                }
            '''
        })
        time.sleep(1.5)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\citizen_report_modal_real.png')

        ws.close()
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
