# 📚[Python Selenium 網頁爬蟲基礎 By 彭彭 - YouTube](https://www.youtube.com/watch?v=ff5L6L5MTCw&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=39)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=Options()
options.chrome_executable_path="selenium/chromedriver.exe"
options.binary_location = "../chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source)

lastpage = driver.find_element(By.LINK_TEXT,"‹ 上頁")
lastpage.click()

tags = driver.find_elements(By.CLASS_NAME,"title") # 上述需先引入
# print(tags) # 直接打印是標籤名稱列表
for tag in tags:
    print(tag.text)

driver.close()