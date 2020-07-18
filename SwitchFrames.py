# Assignment4
# goto http://the-internet.herokuapp.com/frames and select the frames link and navigate between frames
# Navigate in nested frames.
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException, NoSuchFrameException


class SwitchFrame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://the-internet.herokuapp.com/frames")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Help(self):
        self.driver.find_element_by_link_text("Nested Frames").click()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_name("frame-top"))
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_name('frame-left'))
            if ("LEFT" in self.driver.page_source):
                self.assertTrue(True)
            else:
                self.assertFalse(False)
        except NoSuchFrameException:
            self.fail("Left Frame does not exist")
        self.driver.switch_to.parent_frame()
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_name("frame-middle"))
            if "MIDDLE" in self.driver.page_source:
                self.assertTrue(True)
            else:
                self.assertFalse(False)
        except NoSuchFrameException:
            self.fail("Middle Frame does not exist")

        self.driver.switch_to.parent_frame()
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_name("frame-right"))
            if "RIGHT" in self.driver.page_source:
                self.assertTrue(True)
            else:
                self.assertFalse(False)
        except NoSuchFrameException:
            self.fail("Right Frame does not exist")

        self.driver.switch_to.parent_frame()
        self.driver.switch_to.parent_frame()
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_name("frame-bottom"))
            if "BOTTOM" in self.driver.page_source:
                self.assertTrue(True)
            else:
                self.assertFalse(False)
        except NoSuchFrameException:
            self.fail("bottom Frame does not exist")

