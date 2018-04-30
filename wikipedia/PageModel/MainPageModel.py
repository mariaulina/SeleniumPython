from selenium import webdriver

import BasePageModel

class MainPageModel(BasePageModel.BasePageModel):

    def Open(self):
        self.driver.get("http://wikipedia.org")

    def EnterSearchString (self, string):

        self.findClickableElementByID('searchInput').send_keys(string);
        self.findClickableElementByXpath('//*[@id="search-form"]/fieldset/button').click();
