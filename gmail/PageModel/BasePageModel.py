from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Base class to initialize the base page that will be called from all pages
class BasePageModel:
    def __init__(self, driver):
        self.driver = driver

    def findClickableElementByXpath(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))