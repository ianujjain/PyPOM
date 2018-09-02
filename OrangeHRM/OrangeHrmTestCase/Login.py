from OrangeHrmPages.PageLogin import PageLogin
import unittest
from selenium import webdriver
import HtmlTestRunner


class Test_TCLogin(unittest.TestCase):
    
    def test_A(self):
        driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POM\Drivers\chromedriver.exe")
        driver.get('https://opensource-demo.orangehrmlive.com/')
        ObjPageLogin = PageLogin(driver)
        ObjPageLogin.Login("Admin","admin123")
        driver.close();
        driver.quit();

    def test_B(self):
        driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POM\Drivers\chromedriver.exe")
        driver.get('https://opensource-demo.orangehrmlive.com/')
        ObjPageLogin = PageLogin(driver)
        ObjPageLogin.Login("Admin","admin123")
        driver.close();
        driver.quit();



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\'),exit=False)