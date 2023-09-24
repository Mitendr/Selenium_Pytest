import time

from Pages.LoginPage import LoginClass
from Pages.AdminPage import AdminClass
from TestCases import BaseTest

class TestAdmin(BaseTest):

    def test_login(self):
        home=LoginClass(self.driver)
        home.adminTest()
        time.sleep(5)