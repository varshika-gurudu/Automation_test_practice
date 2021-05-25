import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.Logger import Log_Generator
from selenium.webdriver.remote.webelement import WebElement

class sign_up:


    logger = Log_Generator.loggen()
    cookie_element_path = '// *[ @ id = "cookieChoiceDismiss"]'
    frame1 = 'frame-one1434677811'
    FirstName_Input = 'RESULT_TextField-1'

    '''def __init__(self, driver):
        self.driver = driver'''

    def set_cookie(self):
        self.cookie_element = self.driver.find_element_by_xpath(self.cookie_element_path)
        if self.cookie_element:
            self.cookie_element.click()
        print('dismissed cookie')

    def set_frame1(self):

        self.frame_volunteer = self.driver.find_element_by_id(self.frame1)
        self.driver.switch_to.frame(self.frame_volunteer)
        print('switching frame success')


    def set_gender_male(self):

        Element = self.driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label')
        actions = ActionChains(self.driver)
        self.driver.execute_script('arguments[0].scrollIntoView();', Element)
        print('element found')
        # time.sleep(1)
        Element.click()
        print('done')

    def set_gender_female(self):

        Element = self.driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[2]/td/label')
        actions = ActionChains(self.driver)
        self.driver.execute_script('arguments[0].scrollIntoView();', Element)
        print('element found')
        #time.sleep(1)
        Element.click()
        print('done')

    def scroll_till_weekday(self):

        CheckBox_elements = self.driver.find_element_by_id('q15')
        actions = ActionChains(self.driver)
        time.sleep(2)
        self.driver.execute_script('arguments[0].scrollIntoView();', CheckBox_elements)
        print('found checkbox')

    def set_weekdays(self):

        checktable = self.driver.find_element_by_xpath('/html/body/form/div[2]/div[17]/table')
        inputchildren = checktable.find_elements_by_css_selector("td label")
        print('done')

        for element in inputchildren: #checks all boxes
            element.click()

            time.sleep(1)
            print('yea')

        for element in inputchildren:#unchecks all boxes
            if element.is_selected():
                element.click()
                time.sleep(1)
                print('undone')



        self.driver.close()



    def set_drop_down(self):

        element = self.driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')

        print(element.text)
        element1 = Select(element)
        element1.select_by_visible_text('Morning')
        time.sleep(1)
        element1.select_by_visible_text('Afternoon')
        time.sleep(1)
        element1.select_by_visible_text('Evening')
        time.sleep(1)

    def set_upload_file(self, file):
        file_upload = self.driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]')
        file_upload.send_keys(file)
        print('done')





























