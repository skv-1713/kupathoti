import puppeteer from 'puppeteer';

(async () => {
  try {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto('http://localhost:5173/', { waitUntil: 'networkidle2' });
    
    // Check what element is at the position of HOW IT WORKS
    const linkInfo = await page.evaluate(() => {
      const link = Array.from(document.querySelectorAll('.nav-links a')).find(a => a.textContent.includes('HOW IT WORKS'));
      if (!link) return { found: false };
      const rect = link.getBoundingClientRect();
      const elemAtPoint = document.elementFromPoint(rect.x + rect.width / 2, rect.y + rect.height / 2);
      return {
        found: true,
        text: link.textContent,
        href: link.getAttribute('href'),
        rect: { x: rect.x, y: rect.y, width: rect.width, height: rect.height },
        pointerEvents: window.getComputedStyle(link).pointerEvents,
        elemAtPointTag: elemAtPoint ? elemAtPoint.tagName : null,
        elemAtPointClass: elemAtPoint ? elemAtPoint.className : null,
        isLinkSameAsPoint: elemAtPoint === link
      };
    });
    console.log('LINK INFO:', JSON.stringify(linkInfo, null, 2));

    // Try clicking
    console.log('Attempting click on HOW IT WORKS...');
    await page.click('.nav-links a:nth-child(2)'); // or find the exact link
    await new Promise(r => setTimeout(r, 1000));
    console.log('Current URL after click:', page.url());

    await browser.close();
  } catch (err) {
    console.error('Error:', err);
  }
})();
