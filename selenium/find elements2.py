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

def scroll_to_end():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(1)
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )
except:
    driver.quit()
else:
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    time.sleep(1)
    search_box.send_keys("selenium")
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)
    time.sleep(1)

    time.sleep(1)
    n = 0
    while n < 2:
        scroll_to_end()
        n += 1
        time.sleep(1)

    results = driver.find_elements(By.CLASS_NAME, "q0vns")
    for result in results:
        header = result.find_element(By.CLASS_NAME, "VuuXrf")
        print(header.text)

    time.sleep(3)
    driver.close()