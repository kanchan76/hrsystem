import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="../resources/chromedriver-83.exe")
# driver = webdriver.Firefox(executable_path="../resources/geckodriver-64bit.exe")

print(type(driver)) # driver represents browser
driver.maximize_window()
driver.get("http://cookbook.seleniumacademy.com/Config.html")
driver.find_element_by_css_selector("input[value='Diesel']").click()
time.sleep(3)
# check the checkbox
airbags = driver.find_element_by_name("airbags")

# checking the checkbox which is unchecked
if not airbags.is_selected():
    airbags.click()
time.sleep(3)

# unchecking the checkbox which is already checked
if airbags.is_selected():
    airbags.click()
time.sleep(3)
driver.quit()

