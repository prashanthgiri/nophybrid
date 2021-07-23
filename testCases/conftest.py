import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(r'D:\Users\PGiri\Documents\drivers\chromedriver.exe')
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Chrome(r'D:\Users\PGiri\Documents\drivers\chromedriver.exe')
    return driver


def pytest_addoption(parser):   # this will get the value from cli/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return browser value to setup
    return request.config.getoption("--browser")

########### pytest HTML Report ##########
# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']= 'nophybrid'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='prashanth'

#It s=is hook for delete/Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)