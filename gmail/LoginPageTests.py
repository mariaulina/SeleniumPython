'''

Gmail Login Page Test Cases
author: Maria Ulina

'''

import unittest
from selenium import webdriver
from LoginPageModel import LoginPageModel

class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_EmptyUsername(self):
        loginPage = LoginPageModel(self.driver)
        loginPage.Open();
        loginPage.EnterUserName("")

        assert "Enter an email or phone number" in self.driver.page_source

    def test_WrongUsername(self):
        loginPage = LoginPageModel(self.driver)
        loginPage.Open();
        loginPage.EnterUserName("~~invalid_username_masha.ulina~~")

        assert "Couldn't find your Google Account" in self.driver.page_source

    def test_WrongPassword(self):
        loginPage = LoginPageModel(self.driver)
        loginPage.Open();
        loginPage.EnterUserName("masha.ulina")
        loginPage.EnterPassword("~~wrong-password-maria.ulina~~")

        assert "Couldn't find your Google Account" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

# driver = webdriver.Chrome()
#
# loginPage = LoginPageModel(driver)
# loginPage.Open();
# loginPage.EnterUserName("")
#
# assert "Enter an email or phone number1" in driver.page_source

if __name__ == "__main__":
    unittest.main()