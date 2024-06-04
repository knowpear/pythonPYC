from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options=Options()
options.chrome_executable_path="./chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

try:
    # Wait until the element with ID 'myElement' is present in the DOM and visible on the page.
    # Will wait for a maximum of 10 seconds.
    # 🐾似乎不支持XPATH
    element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "title = Search by voice"))
    )
# except ???:
#     print("执行了")
# else:
#     print("超时了")
finally:
    print("finally")
    driver.quit()


driver.close()