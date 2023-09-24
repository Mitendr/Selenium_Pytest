from Pages.Basepage import BaseClass


class AdminClass(BaseClass):
    def __init__(self,driver):
        super().__init__(driver)

    def admin_data(self):

        self.click("Admin_xpath")
        self.click("Add_button_xpath")
        self.click("user_role_xpath")
        self.click("user_role_Admin_xpath")