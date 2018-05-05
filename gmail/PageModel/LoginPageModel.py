from selenium import webdriver

import BasePageModel

# Gmail login page model
class LoginPageModel(BasePageModel.BasePageModel):

    def Open(self):
        self.driver.get("http://gmail.com")

    def EnterUserName (self, username):

        self.findClickableElementByXpath('//*[@id="identifierId"]').send_keys(username);
        self.findClickableElementByXpath('//*[@id="identifierNext"]/content/span').click();

    def EnterPassword(self, password):

        self.findClickableElementByXpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password);
        self.findClickableElementByXpath('//*[@id="passwordNext"]/content/span').click();
