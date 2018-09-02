from Locatars import Login
from WebPages import Page


#from selenium.webdriver.common.keys import Key
class PageLogin(Page.Page):

    def __init__(self, driver):
        self.LoginLocator = Login
        super().__init__(driver)

    def EnterUserName(self, username):
        self.FindElement(*self.LoginLocator.Login.UserName).send_keys(username)

    def EnterPassword(self, password):
        self.FindElement(*self.LoginLocator.Login.Password).send_keys(password)

    def ClickOnSubmit(self):
        self.FindElement(*self.LoginLocator.Login.Submit).click()

    def Login(self,username,password):
        self.EnterUserName(username)
        self.EnterPassword(password)
        self.ClickOnSubmit();


