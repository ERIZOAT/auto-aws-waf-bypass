const puppeteer = require("puppeteer");

(async () => {
  const pathToExtension = "/path/to/your/capsolver_extension_folder"; // Update this path
  const browser = await puppeteer.launch({
    headless: false,
    args: [
      `--disable-extensions-except=${pathToExtension}`,
      `--load-extension=${pathToExtension}`,
    ],
  });
  const page = await browser.newPage();
  await page.goto("https://your-target-website.com"); // Replace with your target URL
})();

