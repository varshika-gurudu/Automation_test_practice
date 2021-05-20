import pyselenium
from selenium import webdriver
from utilities.Logger import Log_Generator
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from TestCases_signup.check_characters import check_char
import time
import string



class Test_title:
    base_url = ReadConfig.getApplicationURL()
    logger = Log_Generator.loggen()
    check_character = check_char()


    def test_signup_title(self, setup):
        self.logger.info('******* Test Title ***********')
        self.driver = setup
        self.logger.info('******** Launching browser *********')
        self.driver.get(self.base_url)
        self.logger.info('******** opening application url *********')
        self.driver.maximize_window()
        time.sleep(2)
        print(self.driver.current_url) # prints current url
        original_title = self.driver.title
        # self.driver.implicitly_wait(10)
        self.driver.close()
        if original_title == 'Automation Testing Practice':
            self.logger.info('******** It is original title *********')
            assert True
        else:
            assert False


    def test_FirstName(self, setup):

        self.logger.info('*********testing NameField ************')
        self.driver = setup

        self.driver.get(self.base_url)
        time.sleep(1)

        cookie_element_path = self.driver.find_element_by_xpath('// *[ @ id = "cookieChoiceDismiss"]')
        if cookie_element_path:
            cookie_element_path.click()

        print('dismissed cookie')
        frame = self.driver.find_element_by_id('frame-one1434677811')
        self.driver.switch_to.frame(frame)

        FirstName_Input = self.driver.find_element_by_name('RESULT_TextField-1')
        FirstName_Input.is_displayed()
        FirstName_Input.is_enabled()
        FirstName_Input.is_selected()
        check_Fname = FirstName_Input.get_attribute('value')
        Fname_length = len(check_Fname)
        print(Fname_length)
        self.logger.info('******** checking if the FirstName is blank ************')
        if Fname_length == 0:
            print('there is no FirstName')
        else:
            print('there is a name')

        self.logger.info('******** FirstName is blank success************')
        print(check_Fname)


        try:
            FirstName_Input.click()
            print('element is clickable')
        except WebDriverException:
            print('element is not clickable')

        self.logger.info('******First Name is displayed,enabled,selected **********')

        print('displayed')
        FirstName_Input.clear()
        First_name = 'varshi1@ka'
        for i in First_name:
            FirstName_Input.send_keys(i)
            #time.sleep()
        #time.sleep(5)


        self.check_character.check_special_char(First_name)
        self.check_character.check_numeric(First_name)
        print('i am success')

        FirstName_Input.clear()

        print(FirstName_Input.text)


        print('element found')

        self.logger.info('*********Finished NameField ************')
        self.driver.close()

















