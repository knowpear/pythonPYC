# https://sahitest.com/demo/iframesTest.htm
# 📚[iframe框架切换_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1VP41167kV?p=25&vd_source=54b152e16c6e182f99df6fd18f1f5d3d)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options=Options()
options.chrome_executable_path="./chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://sahitest.com/demo/iframesTest.htm")
time.sleep(3)
driver.find_element(By.ID, "checkRecord").send_keys("666")

driver.switch_to.frame(1) # 用index切換, 若有的話ID, NAME也支持 # 右面這個iframe在div裏面, 同樣支持
driver.find_element(By.LINK_TEXT, "Link Test").click()
time.sleep(2)

# 切換到上一級ifram
driver.switch_to.parent_frame() # 先返回上級再切換, 不能直接frame間切換

time.sleep(1)
driver.find_element(By.ID, "checkRecord").send_keys("777")

ele = driver.find_element(By.CSS_SELECTOR, "body > iframe") # copy的是iframe的body的selector
driver.switch_to.frame(ele)
driver.find_element(By.LINK_TEXT, "Form Test").click()

time.sleep(3)
driver.close()