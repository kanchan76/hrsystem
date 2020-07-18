# Assignment 6: Dynamic loading
# First scenario
# 1. http://the-internet.herokuapp.com/dynamic_loading/1
# 2. Use implicit Wait - 3 sec
# 3. Click on start button and verify Hello World!
#
# Second scenario
# 1. http://the-internet.herokuapp.com/dynamic_loading/1
# 2. Use implicit Wait - 15 sec
# 3. Click on start button and verify Hello World!
#
# Third scenario
# 1. http://the-internet.herokuapp.com/dynamic_loading/1
# 2. No implicit Wait, No Explicit Wait
# 3. Click on start button and verify Hello World!
#
# Fourth scenario
# 1. http://the-internet.herokuapp.com/dynamic_loading/1
# 2. Use Explicit Wait for 10 seconds
# 3. Click on start button and verify Hello World!

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DynamicLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Nothing for now")


    @classmethod
    def tearDownClass(cls):
        print("Nothing for now")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")

    def tearDown(self):
        self.driver.quit()

    def test_FirstScenario(self): #Failed bcz element was already present at start page
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[contains(text(),"Start")]').click()
        actual_output = self.driver.find_element_by_id("finish").text
        self.assertEqual(actual_output,"Hello World!")

    def test_SecondScenario(self):#Failed bcz element was already present at start page
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath('//*[contains(text(),"Start")]').click()
        actual_output = self.driver.find_element_by_id("finish").text
        self.assertEqual(actual_output,"Hello World!")

    def test_ThirdScenario(self):#Failed bcz element was already present at start page
        self.driver.find_element_by_xpath('//*[contains(text(),"Start")]').click()
        actual_output = self.driver.find_element_by_id("finish").text
        self.assertEqual(actual_output,"Hello World!")

    def test_FourthScenario(self):#passed
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Start')]")))
        self.driver.find_element_by_xpath('//*[contains(text(),"Start")]').click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID,"finish")))
        actual_output = self.driver.find_element_by_id("finish").text
        print(actual_output)
        self.assertEqual(actual_output,"Hello World!")




