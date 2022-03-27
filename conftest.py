import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--background', default = 'true'\
        ,help = 'Background mode: "true" or "false"')

@pytest.fixture(scope = 'function')
def browser(request):
    background = request.config.getoption('--background')
    if background == 'true': print('\n' + 'Browser in background mode')
    else: print('\n' + 'Browser in visible mode')
    tuning = webdriver.ChromeOptions()
    if background == 'true':
        tuning.add_argument('--headless')
    tuning.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options = tuning)
    browser.maximize_window()
    yield browser
    browser.quit()
