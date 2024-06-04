from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# PyCharm有效
# chrome_driver_path = "./chromedriver.exe"
# chrome_binary_location = "./chrome-win64/chrome.exe"
# 🧪PyCharm中以/selenium爲基準, 即當前文件所在目錄📅2024-06-04

# VSCode有效 寫法1
chrome_driver_path = ".\selenium\chromedriver.exe"
chrome_binary_location = ".\selenium\chrome-win64\chrome.exe"
# 🧪VSCode中以/pythonProject爲基準, 即項目根目錄📅2024-06-04

# VSCode有效 寫法2
# chrome_driver_path = "..\pythonProject\selenium\chromedriver.exe"
# chrome_binary_location = "..\pythonProject\selenium\chrome-win64\chrome.exe"

options = Options()
options.binary_location = chrome_binary_location

# Initialize the Service with the path to ChromeDriver
service = Service(chrome_driver_path)

# Create the WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Navigate to Google
driver.get("https://www.google.com")

# Close the browser
driver.quit()