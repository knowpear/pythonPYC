from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options=Options()
options.chrome_executable_path="selenium/chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://docs.python.org/3.12/library/time.html#time.sleep")
def click_btn(title):
    lastpage = driver.find_element(By.LINK_TEXT, title)
    lastpage.click()

def find_tags_by_classname(classname):
    tags = driver.find_elements(By.CLASS_NAME, classname)
    return tags
def scroll_to_end():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(1)
n = 0
while n<2:
    scroll_to_end()
    n += 1
    time.sleep(1)

# 字符串是拆分開來的, 需要拼接..
tags = find_tags_by_classname("pre") # 但是這種就拆散了
# tags = find_tags_by_classname("sig sig-object py") # 🪲爬不到, 定位錯誤(過大), 標籤無內容
for tag in tags:
    print(tag.text)

driver.close()