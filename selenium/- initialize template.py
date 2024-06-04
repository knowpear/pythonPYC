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
options.chrome_executable_path = "./chromedriver.exe"
options.binary_location = "./chrome-win64/chrome.exe"
# options.add_argument("--enable-chrome-browser-cloud-management")

service = Service()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")



driver.close()