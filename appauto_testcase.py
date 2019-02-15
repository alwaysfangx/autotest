
import os
import time
import unittest
from selenium import webdriver


PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['version'] = '7.0'
        desired_caps['deviceName'] = 'RCIVPVMFTOOZ5LZD'
        desired_caps['appPackage'] = 'com.cleanmaster.mguard_cn'
        desired_caps['appActivity'] = 'com.keniu.security.main.MainActivity'
        desired_caps['app'] = PATH('D:\QQ\\6088.apk')
        #desired_caps['appPackage'] = 'com.android.calculator2'
        #desired_caps['appActivity'] = '.Calculator'
        time.sleep(1)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_login(self):
        time.sleep(10)
        identity = self.driver.find_element_by_class_name('输入CSDN账号').send_keys("test")
        usn = self.driver.find_element_by_class_name('输入密码')
        usn.click()
        usn.send_keys('test1')
        self.driver.find_element_by_class_name('登录').click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
