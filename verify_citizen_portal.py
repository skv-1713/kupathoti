import subprocess, time, json, urllib.request, base64
from websocket import create_connection

def run():
    print('Starting Chrome for Citizen Portal verification...')
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

        def capture_screenshot(filename):
            res = send_cmd('Page.captureScreenshot', {'format': 'png'})
            data = res['result']['data']
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(data))
            print(f'Captured {filename}')

        send_cmd('Page.enable')
        time.sleep(2)

        # 1. Rewards Tab
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const buttons = Array.from(document.querySelectorAll('button'));
                const rewBtn = buttons.find(b => b.textContent.toLowerCase().includes('cleanpoints'));
                if (rewBtn) rewBtn.click();
            '''
        })
        time.sleep(1)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\citizen_rewards_impact.png')

        # 2. Open Report Waste Modal
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const buttons = Array.from(document.querySelectorAll('button'));
                const repBtn = buttons.find(b => b.textContent.toLowerCase().includes('report waste'));
                if (repBtn) repBtn.click();
            '''
        })
        time.sleep(1)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\citizen_report_modal.png')

        # 3. Close modal & Click first report to open Tracker Modal
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const closeBtn = document.querySelector('div[class*="fixed"] button');
                if (closeBtn) closeBtn.click();
            '''
        })
        time.sleep(0.5)

        # Switch back to reports tab
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const buttons = Array.from(document.querySelectorAll('button'));
                const repTab = buttons.find(b => b.textContent.toLowerCase().includes('my reports'));
                if (repTab) repTab.click();
            '''
        })
        time.sleep(0.5)

        # Click first report card
        send_cmd('Runtime.evaluate', {
            'expression': '''
                const card = document.querySelector('div[class*="cursor-pointer"]');
                if (card) card.click();
            '''
        })
        time.sleep(1)
        capture_screenshot(r'C:\Users\ELCOT\OneDrive\Desktop\kupathoti\citizen_tracker_modal.png')

        ws.close()
        print('All modal and tab screenshots captured!')
    finally:
        proc.terminate()

if __name__ == '__main__':
    run()
