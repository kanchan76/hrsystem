import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class AssignmentHrm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once before the  setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_combo(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        username = self.driver.find_element_by_id("txtUsername")
        username.send_keys("Admin")
        password = self.driver.find_element_by_id("txtPassword")
        password.send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        leavellist = self.driver.find_element_by_partial_link_text("Leave List")
        leavellist.click()
        time.sleep(3)
        scheduled = self.driver.find_element_by_id("leaveList_chkSearchFilter_2")
        if not scheduled.is_selected():
            scheduled.click()
        taken = self.driver.find_element_by_id("leaveList_chkSearchFilter_3")
        if not taken.is_selected():
            taken.click()
        pending_for_approval = self.driver.find_element_by_id("leaveList_chkSearchFilter_1")
        if pending_for_approval.is_selected():
            pending_for_approval.click()
        subunit = self.driver.find_element_by_id("leaveList_cmbSubunit")
        subunitselect = Select(subunit)
        subunitselect.select_by_visible_text("IT")
        expected_options = ["All",'Sales','Administration','IT','Finance']
        actual_options = []
        for one_option in subunitselect.options:
            actual_options.append(one_option.text)
        self.assertListEqual(expected_options,actual_options)



