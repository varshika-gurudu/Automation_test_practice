import pyselenium
from selenium import webdriver
from utilities.Logger import Log_Generator
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestCases_signup.check_characters import check_char
from PageObjects.NewWindowsObject import New_windows_obj
from PageObjects.NameObject import sign_up
import time

class Test_NewWindows(New_windows_obj):

    base_url = ReadConfig.getApplicationURL()

    def test_search_element(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        #self.set_cookie()

        self.set_search('Electric')
        time.sleep(2)


    def test_alerts(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)

        self.set_alert()

    def test_date(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        self.set_date('04/07/1994')

    def test_select_menu(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.test_select_menu()



