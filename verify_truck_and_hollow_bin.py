import subprocess, time, json, urllib.request, base64
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
    time.sleep(3.5)

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
            time.sleep(1.2)

        def capture_screenshot(filename):
            res = send_cmd('Page.captureScreenshot', {'format': 'png'})
            data = res['result']['data']
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(data))
            print(f'Captured {filename}')

        send_cmd('Page.enable')

        # 1. Capture Hollow Bin during Phase 01 SENSE (y ~ 600)
        scroll_to(600)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\hollow_bin_sense.png')

        # 2. Capture Truck approaching during early Phase 05 (y ~ 2450)
        scroll_to(2450)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\collect_truck_approaching.png')

        # 3. Capture Truck on site at the bin during Phase 05 COLLECT (y ~ 2650)
        scroll_to(2650)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\collect_truck_onsite.png')

        # 4. Capture Final screen with truck parked (y ~ 3100)
        scroll_to(3100)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\collect_final_truck.png')

        ws.close()
        print('Verification screenshots captured successfully!')
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
