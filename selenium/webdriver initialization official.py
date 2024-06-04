# https://www.selenium.dev/documentation/
# 似乎不用導入? 沒找到此webdriver在哪
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()