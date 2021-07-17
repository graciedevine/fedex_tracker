from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait as W
# from selenium.webdriver.support import expected_conditions as E
# import pyautogui as P
import time

exec_path = r"C:\WebDriver\bin\geckodriver.exe"
URL = r"https://www.fedex.com/en-us/home.html"
tracking_id_link_locator = "#HomeTrackingApp input:nth-child(1)"
search_text = "Banana"

driver = webdriver.Firefox(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()

time.sleep(1)
input_box_element = driver.find_element_by_css_selector(tracking_id_link_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()
# driver.quit()

