from Pages.Basepage import BaseClass
from Pages.AdminPage import AdminClass

class LoginClass(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)

    def login(self):
        self.input_text("userName_xpath","Admin")
        self.input_text("password_xpath","admin123")
        self.click("login_xpath")

    def adminTest(self):

        return AdminClass.admin_data(self.driver)
