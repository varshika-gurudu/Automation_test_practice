import pytest
from selenium import webdriver

'''@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path = 'C:/Users/varsh/Desktop/Automation_test_practice/Drivers/chromedriver.exe')
        print('Launching browser')
        return driver'''

@pytest.fixture()
def setup():
    driver = webdriver.Chrome('C:/Users/varsh/Desktop/TheFirstOne/chromedriver_win32/chromedriver.exe')
    print('Launching chrome browser')
    return driver

