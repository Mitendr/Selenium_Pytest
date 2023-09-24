from selenium import   webdriver
from selenium.webdriver.common.by import By
import pytest




@pytest.fixture(scope="function")
def selenium_driver(request):
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    request.cls.driver=driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



