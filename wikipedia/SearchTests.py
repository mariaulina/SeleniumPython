'''

Wikipedia Search Test Cases
author: Maria Ulina

'''

import unittest
from selenium import webdriver
from MainPageModel import MainPageModel

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_SuccessfulSearch(self):
        page = MainPageModel(self.driver)
        page.Open();
        page.EnterSearchString("python")

        assert "Python (programming language)" in self.driver.page_source

    def test_NonExistingArticleSearch(self):
        page = MainPageModel(self.driver)
        page.Open();
        page.EnterSearchString("~~non-existing-article.masha.ulina~~")

        assert "does not exist" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

# driver = webdriver.Chrome()
# page = MainPageModel(driver)
# page.Open();
# page.EnterSearchString("python")

if __name__ == "__main__":
    unittest.main()