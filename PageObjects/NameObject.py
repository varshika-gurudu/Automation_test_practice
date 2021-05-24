from selenium import webdriver

class sign_up:

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











