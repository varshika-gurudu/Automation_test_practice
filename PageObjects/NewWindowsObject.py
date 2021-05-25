import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from utilities.Logger import Log_Generator
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


class New_windows_obj:

    def set_search(self, word):
        search_text = self.driver.find_element_by_xpath('//*[@id="Wikipedia1_wikipedia-search-input"]')
        search_text.send_keys(word)
        print(search_text.get_attribute('value'))
        search_button = self.driver.find_element_by_xpath('//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')
        search_button.click()
        print('done')
        time.sleep(2)
        search_result_links = self.driver.find_elements_by_xpath('//*[@id="wikipedia-search-result-link"]/a')
        for link in search_result_links[0:5:2]:
            link.click()


    def set_alert(self):
        alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
        alert_button.click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        alert_button = self.driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
        alert_button.click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()

    def set_date(self, date):

        date_input = self.driver.find_element_by_xpath('//*[@id="datepicker"]')
        date_input.send_keys(date)
        time.sleep(2)
        date_input.send_keys(Keys.ENTER)
        print('enter')
        time.sleep(2)

    def select_menu(self):
        speed_input = self.driver.find_element_by_xpath('//*[@id="speed"]')
        print(speed_input.text)
        select_speed_input = select(speed_input)
        select_speed_input.select_by_index_value('2')
        time.sleep(2)












