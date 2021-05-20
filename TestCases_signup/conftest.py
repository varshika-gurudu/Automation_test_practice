import pytest
from selenium import webdriver
import string


@pytest.fixture()
def setup():
    driver = webdriver.Chrome('C:/Users/varsh/Desktop/TheFirstOne/chromedriver_win32/chromedriver.exe')
    print('Launching chrome browser')
    return driver







# these methods helps in returning browser
def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# It is hook to generate html reports
# customizable
def pytest_configure(config):
    config._metadata['Project Name'] = 'Automation_test_practice'
    config._metadata['Module Name'] = 'Volunteer sign up'
    config._metadata['Tester'] = 'Varshika'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
