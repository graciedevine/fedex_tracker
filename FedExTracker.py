from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains as A

exec_path = r"C:\WebDriver\bin\chromedriver.exe"
URL = r"https://www.fedex.com/en-us/home.html"
wait_time_out = 30

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=exec_path)
wait_variable = W(driver, wait_time_out)
driver.get(URL)

tracking_css_locator = "#HomeTrackingApp input:nth-child(1)"
search_text = "923767089915"

input_box_element = driver.find_element_by_css_selector(tracking_css_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()

track_button = wait_variable.until(
    E.presence_of_element_located((By.ID, "btnSingleTrack"))
)

a = A(driver)
a.move_to_element(track_button)
a.click(track_button)
a.perform()

# full_details_button = wait_variable.until(
#     E.presence_of_element_located(
#         (
#             By.CLASS_NAME,
#             "redesignSnapshotTVC fxg-tracking-app__more-detail fxg-link fxg-link--blue fxg-link--carrot",
#         )
#     )
# )
# a.move_to_element(full_details_button)
# a.click(full_details_button)
# a.perform()
