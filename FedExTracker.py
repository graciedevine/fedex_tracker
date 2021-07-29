from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains as A
import pyautogui as P
import time

exec_path = r"C:\WebDriver\bin\chromedriver.exe"
URL = r"https://www.fedex.com/en-us/home.html"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
tracking_css_locator = "#HomeTrackingApp input:nth-child(1)"
search_text = "923767089915"
heading_css_locator = "h2.fxg-title--mobile-align-center"
wait_time_out = 5

driver = webdriver.Chrome(options=options, executable_path=exec_path)
wait_variable = W(driver, wait_time_out)
driver.get(URL)
driver.maximize_window()
heading_element = wait_variable.until(
    E.presence_of_element_located((By.CSS_SELECTOR, heading_css_locator))
)
track_button = wait_variable.until(
    E.presence_of_element_located((By.ID, "btnSingleTrack"))
)

input_box_element = driver.find_element_by_css_selector(tracking_css_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()


a = A(driver)
a.double_click(heading_element)
a.move_to_element_with_offset(track_button, 0, 0)
a.click(track_button)
a.perform()

# obtain_pod_button = driver.find_element_by_link_text("OBTAIN PROOF OF DELIVERY").click()

# time.sleep(5)
# x, y = P.position()
# print("X is ", str(x), "Y is ", str(y))

P.scroll(-3)
P.moveTo(944, 768, 3)
P.leftClick()
