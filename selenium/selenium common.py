# import八股文
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

# 實例化Options()
options=Options() # 完整寫法 options = webdriver.ChromeOptions()
options.chrome_executable_path="selenium/chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"

# 實例化Service()
service = Service() # 完整寫法 service = webdriver.ChromeService()
# service.executable_path = "chromedriver.exe" # 路徑似乎在Options()定義也可
# service=Service(executable_path="chromedriver.exe") # ⭐上述兩句的合寫

# 調用webdriver
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window() # 最大化

driver.get("https://www.google.com")

# 截圖
# driver.save_screenshot("gscr.png")

# title
print(driver.title)


time.sleep(3)

driver.close()