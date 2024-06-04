# https://sahitest.com/demo/selectTest.htm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

options=Options()
options.chrome_executable_path="./chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://sahitest.com/demo/selectTest.htm")
time.sleep(2)
sel = driver.find_element(By.XPATH, '//*[@id="testInputEvent"]')
sel_new = Select(sel) # 實例化

# sel_new.select_by_value()
# sel_new.select_by_visible_text() # 可見文字

sel_new.select_by_index(0) # 🧑🏻‍🏫continue

# iterate method 1
for option in sel_new.options:
    print(option.text)

# iterate method 2
for i in range(len(sel_new.options)):
    # option_text = sel_new.options[i].get_property("text")
    option_text = sel_new.options[i].get_attribute("text")
    print(option_text)

driver.close()