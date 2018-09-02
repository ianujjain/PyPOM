from WebPageEntities.Login import Login
from WebBasePages.PageBase import Page
class LoginPage(Page):

    def __init__(self, driver):
        self.Locator = Login
        super().__init__(driver)

    def EnterUserName(self, username):
        self.FindElement(*self.Locator.UserName).send_keys(username)
        

    def EnterPassword(self, password):
        self.FindElement(*self.Locator.Password).send_keys(password)

    def ClickOnSubmit(self):
        self.FindElement(*self.Locator.Submit).click()

    def Login(self,username,password):
        self.EnterUserName(username)
        self.EnterPassword(password)
        self.ClickOnSubmit();