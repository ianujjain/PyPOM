class Page():
    def __init__(self, driver):
        self.Driver     = driver

    def FindElement(self, *locator):
        return self.Driver.find_element(*locator)

    def FindElements(self, *locator):
        return self.Driver.find_element(*locator)
        


