# Assignment3(Most Important Assignment for entire training):
# - go to triphobo.com website
# - Click "Later" in be updated box (this may not appear, then ignore)
# - Click on "PLAN YOUR NEXT VACATION" button on the homepage
# - Type Where do you want to go? field, Houston in Texas
# - Select Start and End date of your journey
# - Click on button "Start Planning"
# - Click on "Next - About Your Trip"
# - Click on "Suggest an itinerary with "Things to do ""
# - Click on "Next" thrice
# - Click on "Wandering Solo"
# - Click on "Next Trip Overview"
# - Click on "Editable View"
# - Drag "Children's museum to day 3"
# - Click on Save plan -> Finish Planning
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from first_selenium_test.web_table_alternate import WebTable_Optimized


class Triphobo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver,25)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.triphobo.com/")

    def tearDown(self):
        print("Nothing for now")

    def test_triphobo(self):

        self.driver.find_element_by_id("plan-my-trip").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//input[@placeholder="Where do you want to go?"]')))
        self.driver.find_element_by_xpath('//input[@placeholder="Where do you want to go?"]').send_keys("Houston")
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Texas')]")))
        builder = ActionChains(self.driver)
        builder.move_to_element(self.driver.find_element_by_id("js-suggestions")).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath("//span[contains(text(),'Texas')]"))
        # builder.click(self.driver.find_element_by_id("dp1591935964752")).move_to_element(self.driver.find_element_by_link_text("17")).click()
        self.driver.find_element_by_xpath('//div[@class="form-control start-end-date-control calendar"]/i[@class="c-icon js_calendar_icon"]').click()
        calendarleft = WebTable_Optimized(self.driver.find_element_by_xpath('//div[@class="ui-datepicker-group ui-datepicker-group-first"]/table[@class="ui-datepicker-calendar"]'))
        # self.select_cell(calendar)
        calendarleft.select_cell_element(3,3).click()
        calendarright = WebTable_Optimized(self.driver.find_element_by_xpath('//div[@class="ui-datepicker-group ui-datepicker-group-last"]/table[@class="ui-datepicker-calendar"]'))
        calendarright.select_cell_element(3,6).click()
        #startplanning = self.driver.find_element_by_xpath("//*[contains(text(),'Start Planning')]")
        self.wait.until(expected_conditions.invisibility_of_element_located((By.XPATH,'//div[@class="ui-datepicker-group ui-datepicker-group-last"]/table[@class="ui-datepicker-calendar"]')))
        self.driver.find_element_by_xpath("//span[@class = 'button p-color full-width start-planning']").click()
        #self.driver.execute_script("arguments[0].click();", startplanning)
        time.sleep(5)
        builder = ActionChains(self.driver)
        next = self.driver.find_element_by_xpath("//span[@id='js_city_next_step_title'][contains(text(),'Next')]")
        self.wait.until(expected_conditions.visibility_of(next))
        builder.move_to_element(next).click().perform()
        time.sleep(5)
        self.wait.until(expected_conditions.visibility_of(self.driver.find_element_by_xpath("//div[@class='profile-list']/descendant::div[3]")))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[@class='profile-list']/div[@class='profile-item']/following-sibling::*[2]")).click().perform()
        time.sleep(5)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[@class='button s-size p-color as-next js-next-alreadybooked']")))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//span[@class='button s-size p-color as-next js-next-alreadybooked']")).click().perform()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='add-transportation-accommodation']")))
        self.driver.execute_script("arguments[0].click();",self.driver.find_element_by_xpath("//div[@class='add-transportation-accommodation']/descendant::*[last()]"))
        #ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[@class='add-transportation-accommodation']/descendant::*[last()]")).click().perform()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='custom-acc-form']")))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath("//div[@class='custom-acc-form']/descendant::*[last()]"))
       # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[@class='custom-acc-form']/descendant::*[last()]")).click().perform()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[contains(text(),"Who are you traveling with?")]')))
       # ActionChains(self.driver).move_to_element((self.driver.find_element_by_xpath("//div[@class='entry-points solo-point  ']"))).click()
        self.driver.execute_script("arguments[0].click();",self.driver.find_element_by_xpath("//div[@class='entry-points solo-point  ']"))
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//span[@id="js_city_next_step_title"]')))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//span[@id="js_city_next_step_title"]')).click().perform()
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Editable view')]")))
        #ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//span[contains(text(),'Editable view')]")).click().perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath("//span[contains(text(),'Editable view')]"))
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@title='Childrens Museum Of Houston']")))
        ActionChains(self.driver).drag_and_drop(self.driver.find_element_by_xpath("//div[@title='Childrens Museum Of Houston']"),self.driver.find_element_by_xpath('//div[@class="fc-event-container"]')).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//div[@class='plan-save-dropdown-holder']")).move_to_element(self.driver.find_element_by_xpath("//li[@class='item js-finish-planning']")).click().perform()








