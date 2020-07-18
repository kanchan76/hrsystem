import unittest

from selenium import webdriver
from selenium.webdriver.support.select import Select


class ToolsQa(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_assignment(self):
        self.driver.get("http://www.demoqa.com/automation-practice-form")
        firstname = self.driver.find_element_by_id("firstName")
        firstname.send_keys("Uday")
        surname= self.driver.find_element_by_id("lastName")
        surname.send_keys("Gonnade")
        print(firstname.get_attribute("value"))
        print(surname.get_attribute("value"))
        self.driver.find_element_by_xpath('//label[@for="gender-radio-1"]').click()
        sportsbox = self.driver.find_element_by_xpath('//label[@for="hobbies-checkbox-1"]')
        if not sportsbox.is_selected():
            sportsbox.click()
        state = self.driver.find_element_by_id("state")
        state.send_keys("Rajasthan")




        



