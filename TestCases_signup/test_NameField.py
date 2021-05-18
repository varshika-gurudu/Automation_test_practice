import pytest
from selenium import webdriver
from utilities.Logger import Log_Generator
from utilities.readProperties import ReadConfig



class Test_title:
    base_url = ReadConfig.getApplicationURL()

    logger = Log_Generator.loggen()

    def test_signup_title(self, setup):
        self.driver = setup
        self.logger.info('hey I am working')
        self.driver.get(self.base_url)





