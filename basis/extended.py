from .main import MainSet
from data.locator import ScriptLocator
from data.locator import ProjectLocator

class ExtendedSet(MainSet):

    def go_to_megafon_project(self):
        self.find_and_click(*ProjectLocator.PROJECT_MENU)
        self.find_and_click(*ProjectLocator.PROJECT_ALL)
        self.find_and_click(*ProjectLocator.PROJECT_MEGAFON)
        assert self.text_present(*ProjectLocator.PROJECT_PAGE_MARKER, 'megafon')\
            ,'Megafon project page NOT FOUND'

    def go_to_megafon_script(self):
        self.find_and_click(*ScriptLocator.SCRIPT_MEGAFON_ALL)
        assert self.text_present(*ScriptLocator.SCRIPT_PAGE_MARKER, 'Scripts')\
                ,'Megafon script page NOT FOUND'

    def archiving_megaphone_script(self):
        self.find_and_mark_checkbox(*ScriptLocator.SCRIPT_MEGAFON_SELECT)
        assert self.element_active(*ScriptLocator.SCRIPT_DELETE)\
            ,'Delete button NOT ACTIVE'
        self.find_and_click(*ScriptLocator.SCRIPT_ARCHIVE)
        self.find_and_click(*ScriptLocator.SCRIPT_ALERT_OK)
        assert self.element_not_present\
            (*ScriptLocator.SCRIPT_MEGAFON_SELECT),'Megafon script NOT ARCHIVED'

    def unarchiving_megaphone_script(self):
        self.find_and_click(*ScriptLocator.SCRIPT_SHOW_ARCHIVED)
        self.find_and_mark_checkbox(*ScriptLocator.SCRIPT_MEGAFON_SELECT)
        assert self.element_active(*ScriptLocator.SCRIPT_DELETE)\
            ,'Delete button NOT ACTIVE'
        self.find_and_click(*ScriptLocator.SCRIPT_UNARCHIVE)
        self.find_and_click(*ScriptLocator.SCRIPT_ALERT_OK)
        assert self.element_disappeared\
            (*ScriptLocator.SCRIPT_MEGAFON_SELECT),'Megafon script NOT UNARCHIVED'
        self.find_and_click(*ScriptLocator.SCRIPT_SHOW_ARCHIVED)
        assert self.element_present\
            (*ScriptLocator.SCRIPT_MEGAFON_SELECT),'Megafon script NOT UNARCHIVED'
