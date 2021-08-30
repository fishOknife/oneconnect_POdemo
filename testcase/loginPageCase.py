from ddt import ddt, data, unpack
import sys
import time
import unittest
from selenium import webdriver
from webPage.loginPage import LoginClass
from baseMethod.useExcel import get_excel_data

FilePath = sys.path[1] + r"\testData\testData.xlsx"
print(FilePath)
SheetName = "登录"
test_data = get_excel_data(FilePath, SheetName)
print("准备的测试数据：", test_data)


@ddt
class TestBaiDu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://1.117.169.63/myapps/login.html"
        # cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Edge()

        cls.driver.implicitly_wait(10)

        # FilePath = sys.path[1] + r"\testData\testData.xlsx"
        # print(FilePath)
        # SheetName = "登录"
        # cls.test_data = get_excel_data(FilePath, SheetName)
        # print("准备的测试数据：",cls.test_data)

    def setUp(self) -> None:
        # 准备测试数据
        # self.oneCase = self.test_data.pop(0)
        # self.url = self.oneCase["url"]
        # self.username = self.oneCase["username"]
        # self.password = self.oneCase["password"]
        # self.assertInfo = self.oneCase["responseData"]

        # 创建登录页面对象
        self.loginPageObject = LoginClass(self.driver)
        self.driver.get(self.url)
        time.sleep(2)

    @data(*test_data)
    @unpack
    def test_0_case(self, username, password, assertInfo):
        # """账号、密码为空"""
        self.loginPageObject.find_username_element().clear()
        self.loginPageObject.find_username_element().send_keys(username)
        self.loginPageObject.find_password_element().clear()
        self.loginPageObject.find_password_element().send_keys(password)
        self.loginPageObject.find_submit_element().click()
        time.sleep(1)
        # 断言
        assert_info = self.loginPageObject.get_alert_info()
        self.assertEqual(assert_info, assertInfo)

    #
    # def test_1_case(self):
    #     """账号、密码为空"""
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_2_case(self):
    #     """账号为空"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #     # 截屏(有alter弹窗不能截屏）
    #     self.loginPageObject.get_screen_shot_file_path()
    #
    # def test_3_case(self):
    #     """密码为空"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_4_case(self):
    #     """账号格式不正确"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_5_case(self):
    #     """账号格式不正确"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_6_case(self):
    #     """账号格式不正确"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_7_case(self):
    #     """账号格式不正确"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)
    #
    # def test_8_case(self):
    #     """账号格式不正确"""
    #     # 操作页面
    #     self.loginPageObject.find_username_element().clear()
    #     self.loginPageObject.find_username_element().send_keys(self.username)
    #     self.loginPageObject.find_password_element().clear()
    #     self.loginPageObject.find_password_element().send_keys(self.password)
    #     self.loginPageObject.find_submit_element().click()
    #     time.sleep(1)
    #     # 断言
    #     assert_info = self.loginPageObject.get_alert_info()
    #     self.assertEqual(assert_info, self.assertInfo)

    def tearDown(self) -> None:
        pass
        # self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # pass
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
