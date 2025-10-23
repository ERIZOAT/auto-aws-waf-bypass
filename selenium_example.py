from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("./capsolver_extension.zip")  # Path to the zipped extension file
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://your-target-website.com") # Replace with your target URL

