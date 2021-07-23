from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import pyautogui as P
import time

exec_path = r"C:\WebDriver\bin\chromedriver.exe"
URL = r"https://www.fedex.com/en-us/home.html"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options, executable_path=exec_path)
driver.get(URL)
driver.maximize_window()

time.sleep(5)
x, y = P.position()
print("X is ", str(x), "Y is ", str(y))
