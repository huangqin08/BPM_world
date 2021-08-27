'''
Code description：save all driver info
Create time：
Developer：
'''

from selenium import webdriver
import logging
import sys
from test_cases.Models.logtest import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class WDriver(object):
    # Firefox driver
    def fireFoxDriver(self):
        """
       :return:
       """
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '%s:found the Firefox driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver

    # chrom driver
    def chromeDriver(self):
        """
       :return:
        """
        try:
            # option = webdriver.ChromeOptions()# 实现不打开浏览器 执行web自动化测试脚本
            # option.add_argument('headless')#
            # self.driver = webdriver.Chrome(chrome_options=option)
            self.driver = webdriver.Chrome()
        except Exception as e:
            log.logger.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '%s:found the chrome driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.driver


if __name__ == '__main__':
    WDrive = WDriver()
    WDrive.chromeDriver()
