from selenium import webdriver
import unittest
from TranslatePageModel import TranslatePageModel

class TestGoogleTranslate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.pageModel = TranslatePageModel(self.driver)
        self.pageModel.Open()

    def test_PageTitle(self):
        assert self.driver.title == 'Google Translate'

    def test_Translation(self):
        self.pageModel.SelectLanguage('Russian')
        assert self.pageModel.Translate('Good Morning!') == 'Доброе утро!'

    def test_TranslationOnThePage(self):
        self.pageModel.SelectLanguage('Russian')
        self.pageModel.Translate('Good Morning!')
        Result = self.pageModel.GetTranslation()
        assert Result[0] == 'Доброе утро!' and Result[1] == 'Good morning!'

    def test_SuggestEditMessage(self):
        self.pageModel.SelectLanguage('Russian')
        self.pageModel.Translate('Good Morning!')
        self.pageModel.SuggestAnEdit()
        assert self.pageModel.GetSuggestEditMessage() == 'Your contribution will be used to improve translation quality and may be shown to users anonymously'

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
