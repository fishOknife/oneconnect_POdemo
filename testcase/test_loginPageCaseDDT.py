from ddt import ddt, data, unpack
import sys
import time
import unittest
from selenium import webdriver
from webPage.loginPage import LoginClass
from baseMethod.useExcel import get_excel_data

FilePath = sys.path[1] + r"\testData\testData.xlsx"
# print(FilePath)
SheetName = "登录"
test_data = get_excel_data(FilePath, SheetName)


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://1.117.169.63/myapps/login.html"
        cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)

    def setUp(self) -> None:
        # 创建登录页面对象
        self.loginPageObject = LoginClass(self.driver)
        self.driver.get(self.url)
        time.sleep(2)

    @data(*test_data)
    @unpack
    def test_0_case(self, username, password, target, assertInfo):
        self.loginPageObject.find_username_element().clear()
        self.loginPageObject.find_username_element().send_keys(username)
        self.loginPageObject.find_password_element().clear()
        self.loginPageObject.find_password_element().send_keys(password)
        self.loginPageObject.find_submit_element().click()
        time.sleep(1)
        # 断言
        assert_info = self.loginPageObject.get_page_info(target)
        self.assertEqual(assert_info, assertInfo)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
