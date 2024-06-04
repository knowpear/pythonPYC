# 🐾def函數
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
def click_btn(title): # 傳參元素標題, 查找並點擊
    lastpage = driver.find_element(By.LINK_TEXT, title)
    lastpage.click()

def find_tags_by_classname(classname):
    tags = driver.find_elements(By.CLASS_NAME, classname)
    return tags

i = 0
while i <= 2: # 循環3次
    click_btn("‹ 上頁")

    tags = find_tags_by_classname("title") # 接收返回值, 此tags不同於彼tags
    for tag in tags:
        print(tag.text)
    i+=1

driver.close()