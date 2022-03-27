import os
from dotenv import load_dotenv
from data.locator import LoginLocator
from data.locator import SidebarLocator
from data.locator import MarkerLocator
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
 
    def open_page(self):
        self.browser.get(self.url)
        assert self.url in self.browser.current_url, 'Page NOT OPEN'

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

    def text_present(self, how, what, text, timeout = 4):
        assert self.element_present(how, what), 'Page element NOT FOUND'
        try: WebDriverWait(self.browser, timeout).until_not\
            (EC.text_to_be_present_in_element((how, what), 'Loading...'))
        except TimeoutException:
            raise AssertionError('Checked text NOT READY')
        line = self.browser.find_element(how, what).text
        print('Text check started')
        print('Expected text: ', text)
        print('Actual text:   ', line)
        if line == text: return True
        else: return False

    def check_marker_user_login(self):
        assert self.element_present(*MarkerLocator.MARKER_USER_LOGIN)\
            ,'User NOT AUTHORIZED'

    def check_marker_project(self, text):
        assert self.text_present(*MarkerLocator.MARKER_PROJECT, text + '·')\
            ,f'{text} project NOT FOUND'

    def check_marker_section(self, text):
        assert self.text_present(*MarkerLocator.MARKER_SECTION, text)\
            ,f'{text} section NOT FOUND'

    def check_marker_subsection(self, text):
        assert self.text_present(*MarkerLocator.MARKER_SUBSECTION, '·' + text)\
            ,f'{text} subsection NOT FOUND'

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

    def user_login(self):
        self.find_and_send_keys(*LoginLocator.LOGIN_USERNAME, TEST_USERNAME)
        self.find_and_send_keys(*LoginLocator.LOGIN_PASSWORD, TEST_PASSWORD)
        self.find_and_click(*LoginLocator.LOGIN_SUBMIT)
        self.check_marker_user_login()

    def sidebar_click_scripts(self):
        self.find_and_click(*SidebarLocator.SIDEBAR_DIALOGUE)

    def sidebar_click_builds(self):
        self.find_and_click(*SidebarLocator.SIDEBAR_AGENT)
        self.find_and_click(*SidebarLocator.SIDEBAR_BUILDS)
