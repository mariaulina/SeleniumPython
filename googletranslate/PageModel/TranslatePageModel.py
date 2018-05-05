from selenium import webdriver
import BasePageModel

class TranslatePageModel (BasePageModel.BasePageModel):

    def Open(self):
        self.driver.get ('https://translate.google.com/')


    def SelectLanguage(self, language_name):

        language_dict = {'Russian':'51', 'Danish':'3h', 'Belorussian':'35'}

        xpath = '//*[@id=":' + language_dict[language_name] + '"]/div'

        self.driver.find_element_by_id('gt-tl-gms').click()
        self.findClickableElementByXpath(xpath).click()

    def Translate(self, source_text):

        self.findClickableElementByXpath('//*[@id="source"]').send_keys(source_text)
        return self.findClickableElementByXpath('//*[@id="result_box"]/span').text


    def GetTranslation(self):

        result = [0, 0]
        result[0] = self.driver.find_element_by_xpath('//*[@id="gt-lc"]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]/div').text
        result[1] = self.driver.find_element_by_xpath('//*[@id="gt-lc"]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[3]/div/span').text
        return result

    def SuggestAnEdit(self):
        self.driver.find_element_by_xpath('//*[@id="gt-res-edit"]').click()

    def GetSuggestEditMessage(self):
        return self.findClickableElementByXpath('//*[@id="gt-res-data"]/div[3]/div[2]/div[1]/div').text