from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

options=Options()
options.chrome_executable_path="./chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

acc = "13804333003"
pwd = "Wetakeit0431"

driver.get("https://www.bilibili.com/")
driver.maximize_window()
time.sleep(1)
# 登陆图标
login_icon = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span")
login_icon.click()
time.sleep(2)
# 帐号框
acc_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入账号"]') # 自己編寫的
time.sleep(1)
print(acc_input.get_property("placeholder"))

acc_input.clear()
acc_input.send_keys(acc)

# 未完成
time.sleep(3)

driver.close()