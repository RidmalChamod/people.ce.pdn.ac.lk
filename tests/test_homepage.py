# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

from distutils.command.config import config
import unittest
import webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):

    # HOMEPAGE
    def test_title(self):
        driver = webdriver_functions.getHomepage()
        title = driver.title
        self.assertEqual(title, "People | people.ce.pdn.ac.lk", "Title is not correct")

    def button_test(self, buttonText, buttonURL):
        driver = webdriver_functions.getHomepage()
        homeButton = driver.find_element(by=By.LINK_TEXT, value=buttonText)
        # get link of homeButton
        link = homeButton.get_attribute("href")
        self.assertEqual(link, buttonURL, buttonText + " link is wrong")

    def test_home_button_link(self):
        self.button_test("Home", "http://www.ce.pdn.ac.lk/")

    def test_people_button_link(self):
        self.button_test("People", a_config_test.SERVER_URL)

    def test_academic_staff_button_link(self):
        self.button_test("Academic Staff", a_config_test.SERVER_URL + "staff/academic/")

    def test_temp_academic_staff_button_link(self):
        self.button_test("Temporary Academic Staff", a_config_test.SERVER_URL + "staff/temporary-academic-staff/")

    def test_academic_support_staff_button_link(self):
        self.button_test("Academic Support Staff", a_config_test.SERVER_URL + "staff/academic-support-staff/")

    def test_past_hods_button_link(self):
        self.button_test("Past HoDs", a_config_test.SERVER_URL + "staff/past-heads-of-dep/")

    def test_past_academic_staff_button_link(self):
        self.button_test("Past Academic Staff", a_config_test.SERVER_URL + "staff/academic/past/")

    def test_alumni_button_link(self):
        self.button_test("Alumni", a_config_test.SERVER_URL + "alumni/")

    # TODO: How to test the E19,E18 buttons ? maybe read from the json and do the tests automatically ? and alumni the same way ?

    def test_postgraduate_button_link(self):
        self.button_test("Postgraduate", a_config_test.SERVER_URL + "students/postgraduate/")

    def test_documentation_button_link(self):
        self.button_test("Documentation", a_config_test.SERVER_URL + "documentation/")


if __name__ == '__main__':
    unittest.main()
