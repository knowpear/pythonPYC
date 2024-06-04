# 🦘[Python Selenium Tutorial #4 - ActionChains & Automating Cookie Clicker! - YouTube](https://www.youtube.com/watch?v=OISEEL5eBqg&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=4)
# https://orteil.dashnet.org/cookieclicker/
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

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
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

driver.find_element(By.ID, "langSelect-EN").click()

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]").click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")

for i in range(1, -1, -1):
    items = driver.find_elements(By.ID, "productPrice" + str(i)) # ❗這裏是複數
# items= [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)] # 連寫, ❗單數

actions = ActionChains(driver)
for i in range(500):
    actions.click(cookie)
    actions.perform() # 🪲執行無效, 把其他前置參數都拉進來就好了
    # cookie.click()
    count = int(cookie_count.text.split(" ")[0]) # 以空格分隔, 取前面數字. 🐾這裏是即時獲取, 循環一次獲取一次
    # print(count)
    for item in items:
        value = int(item.text) # 取道具價格
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
time.sleep(10)
driver.quit()