from PhpTravelsPages.PageLogin import PageLogin
import unittest
from selenium import webdriver
import HtmlTestRunner


class Test_TCLogin(unittest.TestCase):
    
    def test_A(self):
        driver = webdriver.Chrome(r"D:\Python\VS\PyPOM\POM\Drivers\chromedriver.exe")
        driver.get('https://www.phptravels.net/admin')
        ObjPageLogin = PageLogin(driver)
        ObjPageLogin.Login("admin@phptravels.com","demoadmin")
        #driver.close();
        #driver.quit();

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\'),exit=False)