import time
import unittest
import HTMLTestRunner


def creat_suite():
    uit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern="test_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            uit.addTest(test_case)
    return uit


if __name__ == "__main__":
    # 相对路径
    screen_shot_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    test_case_path = ".\\testcase"
    report_path = f".\\report\\report_{screen_shot_time}.html"
    suite = creat_suite()
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试结果", description="登录界面测试")
        runner.run(suite)
