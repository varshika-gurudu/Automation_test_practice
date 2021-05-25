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
from PageObjects.NameObject import sign_up
import time

import string


class Test_First_Name:
    base_url = ReadConfig.getApplicationURL()
    logger = Log_Generator.loggen()
    check_character = check_char()


    def test_signup_title(self,setup):
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
        print(FirstName_Field.get_attribute('value'))
        self.logger.info('******** sending keys to First name Field is success************')



        self.logger.info('******** checking if the characters have any special characters ************')
        self.check_character.check_special_char(First_name)


        self.logger.info('******** checking if the characters contains numeric values************')
        self.check_character.check_numeric(First_name)

        self.logger.info('******** First name Field is success************')


        FirstName_Field.clear() # clearing the First name field
        self.logger.info('*********Finished First name Field ************')
        self.driver.close()




class Test_Phone_Field(check_char):

    logger = Log_Generator.loggen()
    base_url = ReadConfig.getApplicationURL()
    logger.info('********* Testing phone Field ***********')

    def test_phone_field(self,setup):
        self.driver = setup
        self.logger.info('*********** Launching browser ***********')
        self.driver.get(self.base_url)
        self.logger.info('*********** opening application URL ***********')
        time.sleep(0.5)

        self.Sign_Up_Form = sign_up(self.driver)
        self.Sign_Up_Form.set_cookie()  # setting up cookie
        self.logger.info('********* setting up cookie is Success ************')
        time.sleep(1)
        print('it is working')

        self.Sign_Up_Form.set_frame1()  # as there are three frames,switching to center frame(volunteer sign up)
        self.logger.info('********* switching to iframe is Success ************')

        self.logger.info('********* Finding the phone field element  ************')
        time.sleep(5)
        phone_field = self.driver.find_element_by_name('RESULT_TextField-3')
        print('phone field')

        self.logger.info('********** testing if the phone field is blank **********')
        test_phone_blank = phone_field.get_attribute('value')
        phone_field_length = (len(test_phone_blank))
        if phone_field_length == 0:
            assert True
            self.logger.info('********** phone field is blank success **********')
        else:
            assert  False

        phone_number = '12345678'
        phone_field.send_keys(phone_number)
        self.driver.implicitly_wait(3)
        self.logger.info('********** checking if phone field has characters **********')
        self.check_characters(phone_number)
        self.logger.info('********** phone field is success **********')
        self.driver.close()

class Test_email(sign_up,check_char):
    logger = Log_Generator.loggen()
    base_url = ReadConfig.getApplicationURL()
    logger.info('********* Testing email Field ***********')

    def test_email_field(self, setup):
        self.driver = setup
        self.logger.info('*********** Launching browser ***********')
        self.driver.get(self.base_url)
        self.logger.info('*********** opening application URL ***********')
        time.sleep(0.5)

        self.Sign_Up_Form = sign_up(self.driver)
        self.Sign_Up_Form.set_cookie()  # setting up cookie
        self.logger.info('********* setting up cookie is Success ************')
        time.sleep(1)
        print('it is working')

        self.Sign_Up_Form.set_frame1()  # as there are three frames,switching to center frame(volunteer sign up)
        self.logger.info('********* switching to iframe is Success ************')

        self.logger.info('********* Finding the phone field element  ************')
        time.sleep(1)
        self.driver.maximize_window()

        email = 'varshika402@gmail.com'
        phone_field = self.driver.find_element_by_name('RESULT_TextField-6')
        #phone_field = self.driver.find_element_by_name('RESULT_TextField-6').send_keys(email)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME,'RESULT_TextField-6'))).click()
        phone_field = self.driver.find_element_by_name('RESULT_TextField-6').send_keys(email)

        time.sleep(3)
        self.driver.execute_script('arguments[0].scrollIntoView();', phone_field)
        print('it is scrollinf')
        time.sleep(3)
        #actions = ActionChains(self.driver)
        #actions.move_to_element(phone_field).perform()
        self.check_email(email)
        self.driver.close()

class Test_Gender(sign_up):
    logger = Log_Generator.loggen()
    base_url = ReadConfig.getApplicationURL()
    logger.info('********* Testing Gender Radio buttons ***********')

    def test_gender(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.set_cookie()
        self.set_frame1()

        self.logger.info('********* Testing Gender Radio buttons ***********')

        self.set_gender_male()
        time.sleep(1)

        self.set_gender_female()
        time.sleep(3)


    def test_WeekDay(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.set_cookie()
        self.set_frame1()

        self.scroll_till_weekday()
        time.sleep(3)
        self.set_weekdays()

    def test_BestTime_contact(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.set_cookie()
        self.set_frame1()

        self.scroll_till_weekday()
        self.set_drop_down()

    def test_upload_file(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.set_cookie()
        self.set_frame1()

        self.set_upload_file('C:/Users/varsh/Desktop/hi.txt')



























































