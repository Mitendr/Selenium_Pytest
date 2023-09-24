import time

from Pages.Basepage import BaseClass
from Pages.LoginPage import LoginClass
from TestCases.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        home=LoginClass(self.driver)
        home.login()
        time.sleep(5)




