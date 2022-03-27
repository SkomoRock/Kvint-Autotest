from .main import MainSet
from data.locator import HistoryLocator
from data.locator import MegafonLocator
from data.locator import PaginationLocator
from data.locator import ProjectLocator
from data.locator import ScriptLocator

class ExtendedSet(MainSet):

    def go_to_megafon_from_main_page(self):
        self.find_and_click(*ProjectLocator.PROJECT_MENU)
        self.find_and_click(*ProjectLocator.PROJECT_ALL)
        self.find_and_click(*ProjectLocator.PROJECT_MEGAFON)
        self.check_marker_project('megafon')

    def check_number_of_megafon_total_calls(self):
        self.find_and_click(*HistoryLocator.CALL_STATUS_MENU)
        self.find_and_click(*HistoryLocator.CALL_STATUS_RESET)
        assert self.text_present(*PaginationLocator.TOTAL_ITEMS\
            ,MegafonLocator.MEGAFON_TOTAL_CALLS)\
            ,'Number of Megafon successful calls DOES NOT MATCH'

    def check_number_of_megafon_success_calls(self):
        self.find_and_click(*HistoryLocator.CALL_STATUS_MENU)
        self.find_and_mark_checkbox(*HistoryLocator.CALL_STATUS_SUCCESS)
        self.find_and_click(*HistoryLocator.CALL_STATUS_OK)
        assert self.text_present(*PaginationLocator.TOTAL_ITEMS\
            ,MegafonLocator.MEGAFON_SUCCESS_CALLS)\
            ,'Number of Megafon successful calls DOES NOT MATCH'

    def start_megafon_script_archiving(self):
        self.find_and_mark_checkbox(*MegafonLocator.MEGAFON_SCRIPT_SELECT)
        assert self.element_active(*ScriptLocator.SCRIPT_DELETE)\
            ,'Delete button NOT ACTIVE'
        self.find_and_click(*ScriptLocator.SCRIPT_ARCHIVE)
        self.find_and_click(*ScriptLocator.SCRIPT_CONFIRM_ARCHIVE)
        assert self.element_not_present\
            (*MegafonLocator.MEGAFON_SCRIPT_SELECT),'Megafon script NOT ARCHIVED'

    def start_megafon_script_unarchiving(self):
        self.find_and_click(*ScriptLocator.SCRIPT_SHOW_ARCHIVED)
        self.find_and_mark_checkbox(*MegafonLocator.MEGAFON_SCRIPT_SELECT)
        assert self.element_active(*ScriptLocator.SCRIPT_DELETE)\
            ,'Delete button NOT ACTIVE'
        self.find_and_click(*ScriptLocator.SCRIPT_UNARCHIVE)
        self.find_and_click(*ScriptLocator.SCRIPT_CONFIRM_UNARCHIVE)
        assert self.element_disappeared\
            (*MegafonLocator.MEGAFON_SCRIPT_SELECT),'Megafon script NOT UNARCHIVED'
        self.find_and_click(*ScriptLocator.SCRIPT_SHOW_ARCHIVED)
        assert self.element_present\
            (*MegafonLocator.MEGAFON_SCRIPT_SELECT),'Megafon script NOT UNARCHIVED'
