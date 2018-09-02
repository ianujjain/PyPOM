from WebPages.LoginPage import PageLogin
import unittest
from selenium import webdriver


class Test_TCLogin(unittest.TestCase):
    def test_A(self):
        driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POMAutomation\Drivers\chromedriver.exe")
        driver.get('https://opensource-demo.orangehrmlive.com/')
        ObjLoginPage = PageLogin(driver)
        ObjLoginPage.Login("Admin","admin123")

if __name__ == '__main__':
    unittest.main(exit=False)