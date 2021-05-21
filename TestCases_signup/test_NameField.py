import pyselenium
from selenium import webdriver
from utilities.Logger import Log_Generator
from utilities.readProperties import ReadConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from TestCases_signup.check_characters import check_char
from PageObjects.NameObject import sign_up
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

        self.logger.info('*********testing First name Field ************')
        self.driver = setup # getting webdriver


        self.driver.get(self.base_url)# getting application url
        self.logger.info('*********getting application URL Success ************')


        self.Sign_Up_Form = sign_up(self.driver)
        self.Sign_Up_Form.set_cookie() # setting up cookie
        self.logger.info('********* setting up cookie is Success ************')
        time.sleep(3)
        print('it is working')

        self.Sign_Up_Form.set_frame1() #as there are three frames,switching to center frame(volunteer sign up)
        self.logger.info('********* switching to iframe is Success ************')



        self.logger.info('********* Finding First name Element  ************')
        FirstName_Field = self.driver.find_element_by_name('RESULT_TextField-1')
        FirstName_Field.is_displayed() #element dispaly
        FirstName_Field.is_enabled() #element enable
        FirstName_Field.is_selected() #element selected
        self.logger.info('********* First name display,enable,selection is success ************')



        self.logger.info('********* checking if the field is blank ************')
        check_Fname = FirstName_Field.get_attribute('value') #getting the value of first name field(it is empty)
        Fname_length = len(check_Fname) # finding length of the value
        print(Fname_length)
        if Fname_length == 0:
            print('there is no FirstName')
            self.logger.info('********* First name field is blank ************')
        else:
            self.logger.info('********* First name field is blank is unsuccess ************')




        self.logger.info('******** checking if the Firstname field is clickable ************')
        try:
            FirstName_Field.click()
            self.logger.info('******** FirstName field clickable success************')

            print('element is clickable')
        except WebDriverException:
            self.logger.info('******** FirstName field  clickable Unsuccess************')

            print('element is not clickable')



        self.logger.info('******** checking if FirstName field is accepting input ************')
        FirstName_Field.clear()
        FirstName_Field.clear()
        self.logger.info('******** sending keys to First name Field ************')
        First_name = 'varshi1@ka'
        for i in First_name: # sending one character for every 0.5 sec
            FirstName_Field.send_keys(i)
            time.sleep(0.5)
        #time.sleep(5)
        self.logger.info('******** sending keys to First name Field is success************')



        self.logger.info('******** checking if the characters have any special characters ************')
        self.check_character.check_special_char(First_name)


        self.logger.info('******** checking if the characters contains numeric values************')
        self.check_character.check_numeric(First_name)

        self.logger.info('******** First name Field is success************')


        FirstName_Field.clear() # clearing the First name field


        self.logger.info('*********Finished First name Field ************')
        self.driver.close()

















