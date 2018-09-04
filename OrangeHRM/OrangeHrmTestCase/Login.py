from OrangeHrmPages.PageLogin import PageLogin
import unittest
from selenium import webdriver
import HtmlTestRunner
import pytest
import time


class Test_TCLogin(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POM\Drivers\chromedriver.exe")
        inst.driver.maximize_window()
        inst.driver.get('https://opensource-demo.orangehrmlive.com/')
        inst.ObjPageLogin = PageLogin(inst.driver)


    def test_ValidateLoginWithInValidUser(self):   
        ErrorMessage = self.ObjPageLogin.InvalidCredentialsLogin("Admin1","admin1231")
        time.sleep(5)
        self.assertEqual(ErrorMessage, "Invalid credentials",'Incorrect Error Message: Invalid credentials')


    def test_ValidateLoginWithValidUser(self):
        self.ObjPageLogin.Login("Admin","admin123")

    #def test_ValidateUsernameCannotBeEmptyErrorMessage(self):
        #ErrorMessage = self.ObjPageLogin.UsernameCannotBeEmptyLogin()
        #self.assertEqual(ErrorMessage, "Username cannot be empty",'Incorrect Error Message: Username cannot be empty')


    @classmethod
    def tearDownClass(inst):
        inst.driver.close()
        inst.driver.quit()
 
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\'),exit=False)