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
options.binary_location = "./chrome-win64/chrome.exe"
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_argument('--no-sandbox')

service = Service()
driver = webdriver.Chrome(service=service, options=options)

# site = "https://lizhi.shop"
# site = "https://app.myshell.ai/chat"
# site = "https://copilot.microsoft.com/"
# site = "https://www.bilibili.com/"

site = input("请输入网址：")
driver.get(site)

def save_cookies():
    driver.get(site)
    driver.maximize_window()
    time.sleep(2)
    # 获取当前会话的所有Cookie
    all_cookies = driver.get_cookies()

    # 将Cookie保存到文件
    with open('cookies.txt', 'w') as file:
        json.dump(all_cookies, file)

    # 关闭webdriver
    driver.quit()

def confirmation():
    while True:
        confirmation = input("请按下 Y 或 N 确认继续：")
        if confirmation.upper() == "Y":
            print("您选择了继续。")
            break
        elif confirmation.upper() == "N":
            print("您选择了取消。")
            break
        else:
            print("无效的输入。")
            continue

# 接收用戶信息
confirmation()
# 执行保存Cookie的函数
save_cookies()