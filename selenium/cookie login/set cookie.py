from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

options=Options()
options.chrome_executable_path= "../chromedriver.exe"
options.binary_location = "../chrome-win64/chrome.exe"
service = Service()
driver = webdriver.Chrome(service=service, options=options)

site = input("请输入网址：")

# site = "https://lizhi.shop"
# site = "https://app.myshell.ai/chat"
# site = "https://copilot.microsoft.com/"
# site = "https://www.bilibili.com/"

def load_cookies_and_login():
    driver.get(site)
    driver.maximize_window()

    # 读取Cookie
    with open('cookies.txt', 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    time.sleep(5)
    # 再次访问网站，现在应该会自动登录
    driver.get(site)

    # 继续你的操作...
    time.sleep(15)

    # 关闭webdriver
    driver.quit()

# 执行加载Cookie并登录的函数
load_cookies_and_login()