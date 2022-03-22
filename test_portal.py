import pytest
from data.locator import LoginLocator
from basis.extended import ExtendedSet

@pytest.fixture(autouse = True)
def test_user_login(browser):
    page = ExtendedSet(browser, LoginLocator.LOGIN_LINK)
    page.open_page()
    page.user_login()

def test_megafon_script_archiving(browser):
    page = ExtendedSet(browser, LoginLocator.LOGIN_LINK)
    page.go_to_megafon_project()
    page.go_to_megafon_script()
    page.megafon_script_archiving()
    page.megafon_script_unarchiving()
