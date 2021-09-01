from baseMethod.outPutLog import Log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    # BasePage封装所有界面都公用的方法。例如driver,find_element等
    # 实例化BasePage类时，事先执行的__init__方法，该方法需要传递参数

    def __init__(self, driver):
        self.driver = driver
        # 创建日志对象
        self.log = Log()

    # 元素定位,替代八大定位
    def find_element(self, *locator):
        self.log.info("开始定位元素")
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((*locator,)), "查找元素超时")
        return self.driver.find_element(*locator)

    def get_alert_info(self):
        self.log.info("获取alter信息")
        WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present(), "查找alter超时")
        assert_info = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return assert_info

    def get_title_info(self):
        self.log.info("获取title信息")
        assert_info = self.driver.title
        return assert_info

    # def get_screen_shot_file_path(self):
    #     screen_shot_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    #     object_path = sys.path[1]
    #     file_path = object_path + f"\screenshot\{screen_shot_time}.png"
    #     return self.driver.get_screenshot_as_file(file_path)

    # def write_logs_to_file(self):
    #     log_file = r"F:\Python38 Project\baiduUiPO\logs\123.txt"
    #     logging.basicConfig(level=logging.debug,
    #                         filename=log_file,
    #                         filemode="a",
    #                         format="%(asctime)s - %(levelname)s: %(message)s")
    #     filehandle = logging.FileHandler(log_file, encoding="utf-8")
    #     logging.getLogger().addHandler(filehandle)
    #     log = logging.exception("手动录入错误信息")
    #     return log
