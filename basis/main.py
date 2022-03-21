import os
from dotenv import load_dotenv
from data.locator import LoginLocator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

TEST_USERNAME = str(os.environ.get('TEST_USERNAME'))
TEST_PASSWORD = str(os.environ.get('TEST_PASSWORD'))

class MainSet():

    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def element_active(self, how, what, timeout = 4):
        try: WebDriverWait(self.browser, timeout)\
            .until(EC.element_to_be_clickable((how, what)))
        except TimeoutException: return False
        return True

    def element_present(self, how, what):
        try: self.browser.find_element(how, what)
        except NoSuchElementException: return False
        return True

    def element_not_present(self, how, what, timeout = 4):
        try: WebDriverWait(self.browser, timeout)\
            .until(EC.presence_of_element_located((how, what)))
        except TimeoutException: return True
        return False

    def element_disappeared(self, how, what, timeout = 4):
        try: WebDriverWait(self.browser, timeout, 1, TimeoutException)\
            .until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException: return False
        return True

    def text_present(self, how, what, text):
        try: line = self.browser.find_element(how, what).text
        finally:
            if line == text: return True
            else: return False

    def find_and_click(self, how, what):
        assert self.element_present(how, what), 'Page element NOT FOUND'
        assert self.element_active(how, what), 'Page element NOT ACTIVE'
        target = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.move_to_element(target).click()
        action.perform()

    def find_and_send_keys(self, how, what, keys):
        assert self.element_present(how, what), 'Page element NOT FOUND'
        assert self.element_active(how, what), 'Page element NOT ACTIVE'
        target = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.send_keys_to_element(target, keys)
        action.perform()

    def find_and_mark_checkbox(self, how, what):
        assert self.element_present(how, what), 'Page element NOT FOUND'
        target = self.browser.find_element(how, what)
        action = ActionChains(self.browser)
        action.move_to_element(target).click()
        action.perform()

    def open_page(self):
        try: self.browser.get(self.url)
        finally: assert self.url in self.browser.current_url, 'Page NOT OPEN'

    def user_login(self):
        try:
            self.find_and_send_keys(*LoginLocator.LOGIN_USERNAME, TEST_USERNAME)
            self.find_and_send_keys(*LoginLocator.LOGIN_PASSWORD, TEST_PASSWORD)
            self.find_and_click(*LoginLocator.LOGIN_SUBMIT)
        finally:
            assert self.element_present(*LoginLocator.LOGIN_USER_MARKER)\
                ,'User NOT AUTHORIZED'
