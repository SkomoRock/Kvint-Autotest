from selenium.webdriver.common.by import By

class HistoryLocator():
    CALL_STATUS_MENU = (By.XPATH, '//th[.//span[text()="Call Status"]]//i')
    CALL_STATUS_OK = (By.XPATH, '//a[text()="OK"]')
    CALL_STATUS_RESET = (By.XPATH, '//a[text()="Reset"]')
    CALL_STATUS_SUCCESS = (By.XPATH, '//li[.//span[text()="success"]]//input')

class LoginLocator():
    LOGIN_LINK = 'https://go.staging.kvint.io'
    LOGIN_USERNAME = (By.TAG_NAME, 'input[data-test-id="username"]')
    LOGIN_PASSWORD = (By.TAG_NAME, 'input[data-test-id="password"]')
    LOGIN_SUBMIT = (By.TAG_NAME, 'button[data-test-id="submit"]')

class MarkerLocator():
    MARKER_USER_LOGIN = (By.CSS_SELECTOR, 'span.ant-avatar-string')
    MARKER_PROJECT = \
        (By.XPATH, '//*[@id="app"]/section/section/div/span[1]')
    MARKER_SECTION = \
        (By.XPATH, '//*[@id="app"]/section/section/div/span[2]')
    MARKER_SUBSECTION = \
        (By.XPATH, '//*[@id="app"]/section/section/div/span[3]') 

class MegafonLocator():
    MEGAFON_HISTORY = 'https://go.staging.kvint.io/megafon/calls/history'
    MEGAFON_HISTORY_FILTER = \
        MEGAFON_HISTORY + '?limit=100&offset=0&start=1638306000&end=1638392399'
    MEGAFON_TOTAL_CALLS = 'Total 562508 items'
    MEGAFON_SUCCESS_CALLS = 'Total 70373 items'
    MEGAFON_SCRIPT_ID = '1648112030'
    MEGAFON_SCRIPT_SELECT = \
        (By.XPATH, f'//tr[.//span[text()={MEGAFON_SCRIPT_ID}]]//input')

class PaginationLocator():
    TOTAL_ITEMS = (By.TAG_NAME, 'div .ant-pagination-total-text')

class ProjectLocator():
    PROJECT_MENU = (By.XPATH, '//*[text()="Projects"]')
    PROJECT_ALL = (By.XPATH, '//*[text()="View all projects"]')
    PROJECT_MEGAFON = \
        (By.CSS_SELECTOR, '.ant-table a[href="/megafon/calls/history"]')

class ScriptLocator():
    SCRIPT_DELETE = (By.XPATH, '//button[span[text()="Delete"]]')
    SCRIPT_ARCHIVE = (By.XPATH, '//button[span[text()="Archive"]]')
    SCRIPT_UNARCHIVE = (By.XPATH, '//button[span[text()="UnArchive"]]')
    SCRIPT_SHOW_ARCHIVED = (By.CSS_SELECTOR, 'button.ant-switch')
    SCRIPT_CONFIRM_ARCHIVE = \
        (By.TAG_NAME, 'button[data-test-id="btn-confirm-archive"]')
    SCRIPT_CONFIRM_UNARCHIVE = \
        (By.TAG_NAME, 'button[data-test-id="btn-confirm-unarchive"]')

class SidebarLocator():
    SIDEBAR_DIALOGUE = (By.TAG_NAME, 'li[data-test-id="sidebarMain-dialogue"]')
    SIDEBAR_AGENT = (By.TAG_NAME, 'li[data-test-id="sidebarMain-agent"]')
    SIDEBAR_BUILDS = (By.TAG_NAME, 'li[data-test-id="sidebarNested-agent-builds"]')
