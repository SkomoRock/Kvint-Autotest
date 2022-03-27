import pytest
from data.locator import LoginLocator
from data.locator import MegafonLocator
from basis.extended import ExtendedSet

@pytest.fixture(autouse = True)
def test_user_login(browser):
    test = ExtendedSet(browser, LoginLocator.LOGIN_LINK)
    test.open_page()
    test.user_login()

def test_megafon_history_filter(browser):
    test = ExtendedSet(browser, MegafonLocator.MEGAFON_HISTORY_FILTER)
    test.open_page()
    test.check_marker_project('megafon')
    test.check_marker_subsection('History')
    test.check_number_of_megafon_total_calls()
    test.check_number_of_megafon_success_calls()
    test.check_number_of_megafon_total_calls()

def test_megafon_script_archiving(browser):
    test = ExtendedSet(browser, MegafonLocator.MEGAFON_HISTORY)
    test.open_page()
    test.check_marker_project('megafon')
    test.check_marker_subsection('History')
    test.sidebar_click_scripts()
    test.check_marker_section('Scripts')
    test.start_megafon_script_archiving()
    test.start_megafon_script_unarchiving()
