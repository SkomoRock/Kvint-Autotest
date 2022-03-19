import pytest
from selenium import webdriver

# only for chrome browser
@pytest.fixture(scope = 'function')
def browser():
    tuning = webdriver.ChromeOptions()
    # enable background mode
    tuning.add_argument('--headless')
    # turn off notifications DevTools
    tuning.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options = tuning)
    browser.maximize_window()
    yield browser
    browser.quit()
