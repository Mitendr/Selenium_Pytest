import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.LogUtil import Logger
from Utilities import configreader

log=Logger(__name__,file_leve=logging.INFO)


class BaseClass:
    def __init__(self,driver):
        self.driver=driver

    def click(self,locator):
        if str(locator).endswith("xpath"):
            self.driver.find_element(By.XPATH,configreader.readconfig("locators",locator)).click()
        elif str(locator).endswith("id"):
            self.driver.find_element(By.ID, configreader.readconfig("locators", locator)).click()
        log.logger.info('clicking on element' + str(locator))



    def input_text(self,locator,text):
        if str(locator).endswith("xpath"):
            self.driver.find_element(By.XPATH,configreader.readconfig("locators",locator)).send_keys(text)
        elif str(locator).endswith("id"):
            self.driver.find_element(By.ID, configreader.readconfig("locators", locator)).send_keys(text)
        log.logger.info('sending text on element' + str(locator))


