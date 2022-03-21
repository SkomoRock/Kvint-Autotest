from selenium.webdriver.common.by import By

class LoginLocator():
    LOGIN_LINK = 'https://go.staging.kvint.io'
    LOGIN_USERNAME = (By.TAG_NAME, 'input[data-test-id="username"]')
    LOGIN_PASSWORD = (By.TAG_NAME, 'input[data-test-id="password"]')
    LOGIN_SUBMIT = (By.TAG_NAME, 'button[data-test-id="submit"]')
    LOGIN_USER_MARKER = (By.CSS_SELECTOR, 'span.ant-avatar-string')

class ProjectLocator():
    PROJECT_MENU = (By.XPATH, '//*[text()="Projects"]')
    PROJECT_ALL = (By.XPATH, '//*[text()="View all projects"]')
    PROJECT_MEGAFON = \
        (By.CSS_SELECTOR, '.ant-table a[href="/megafon/calls/history"]')
    PROJECT_PAGE_MARKER = \
        (By.XPATH, '//*[@id="app"]/section/section/div/span[1]/span[1]')

class ScriptLocator():
    SCRIPT_MEGAFON_ID = '1647507561'
    SCRIPT_MEGAFON_SELECT = \
        (By.XPATH, f'//tr[.//span[text()={SCRIPT_MEGAFON_ID}]]//input')
    SCRIPT_MEGAFON_ALL = \
        (By.CSS_SELECTOR, '.ant-menu a[href="/megafon/dialogue"]')
    SCRIPT_DELETE = (By.XPATH, '//button[span[text()="Delete"]]')
    SCRIPT_ARCHIVE = (By.XPATH, '//button[span[text()="Archive"]]')
    SCRIPT_UNARCHIVE = (By.XPATH, '//button[span[text()="UnArchive"]]')
    SCRIPT_ALERT_OK = (By.XPATH, '//button[span[text()="OK"]]')
    SCRIPT_SHOW_ARCHIVED = (By.CSS_SELECTOR, 'button[role="switch"]')
    SCRIPT_PAGE_MARKER = \
        (By.XPATH, '//*[@id="app"]/section/section/div/span[2]/span')
