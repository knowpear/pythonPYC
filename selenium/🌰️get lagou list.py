# 📚[04 Selenium入门-4_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1DH4y1i7Dm/?p=4&spm_id_from=pageDriver&vd_source=54b152e16c6e182f99df6fd18f1f5d3d)
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
account = "13804333003"
password = "Asd123456!"

driver.get("https://www.lagou.com/")
driver.maximize_window()
time.sleep(3)
login_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[2]/ul/li[1]/a")
time.sleep(1)
login_btn.click()

usepwd_btn = driver.find_element(By.XPATH, '//div[contains(text(),"密码登录")]')
time.sleep(3)
usepwd_btn.click()

time.sleep(1)
account_input = driver.find_element(By.XPATH, '//input[@placeholder="请输入常用手机号/邮箱"]')
account_input.send_keys(account)
time.sleep(1)

password_input = driver.find_element(By.XPATH, "//input[@placeholder='请输入密码']")
password_input.send_keys(password)
time.sleep(1)

agree_check = driver.find_element(By.XPATH, '//div[@class="sc-furwcr bVYGWy"]')
agree_check.click()
time.sleep(1)

login_enter = driver.find_element(By.XPATH, '//span[contains(text(),"登 录")]')
login_enter.click()
# time.sleep(20) # 等待用戶自行輸入驗證碼

WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "我的简历")) # ✌️查找成功, 自動進入下一步
)
time.sleep(2)
search_btn = driver.find_element(By.XPATH, '//input[@id="search_input"]')
time.sleep(1)
search_btn.send_keys("python")
time.sleep(1)
search_btn.send_keys(Keys.ENTER)
time.sleep(8)

# 獲取當前所有打開的選項卡的handles
window_handles = driver.window_handles
# 切換到新的選項卡（假設新選項卡是列表中的最後一個）
driver.switch_to.window(window_handles[-1])

time.sleep(2)
results = driver.find_elements(By.ID, "openWinPostion")
for result in results:
    print(result.text)

time.sleep(5)
driver.close()