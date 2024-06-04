from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # ⭐需要添加的
import time

options=Options()
options.chrome_executable_path="selenium/chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://lizhi.shop/")
account = "daiyigr@qq.com"
password = "Asd123456"

driver.maximize_window()

def click_btn_by_LINK_TEXT(text):
    btn= driver.find_element(By.LINK_TEXT, text)
    btn.click()

# 點擊登陸
time.sleep(1)
click_btn_by_LINK_TEXT("登录 / 注册")

# 點擊密碼登陸
# 手工xpath
# image_element = driver.find_element(By.XPATH, "//img[@src='https://shop-cdn.lizhi.shop/views/lizhi_new/javascript/assets/img/pages/login/Login-Btn-email@2x-v2.png']")
# 🖱️copy xpath
image_element = driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div[5]/div[1]/img")
image_element.click()

# input account
time.sleep(1)
# account_input = driver.find_element(By.CSS_SELECTOR, "[placeholder=请输入手机号 / 邮箱]") # error
account_input = driver.find_element(By.CSS_SELECTOR, "[x-model=userName]")
account_input.send_keys(account)

# input password
time.sleep(1)
account_input = driver.find_element(By.CSS_SELECTOR, "[placeholder=请输入密码]")
account_input.send_keys(password)

# press ENTER
time.sleep(1)
account_input.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()