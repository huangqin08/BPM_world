'''
Code description：test report
Create time：
Developer：
'''
from HTMLTestRunner import HTMLTestRunner
import time
import logging
import unittest
from BeautifulReport import BeautifulReport
import HTMLTestRunner
from config import conf
from test_cases.Models.logtest import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


# 用HTMLTestRunner 实现的测试报告
def test_report():
    """
   :return:
    """
    # 生成测试报告的路径
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = conf.reportPath + r'\report' + currTime + 'result.html'
    try:
        fp = open(fileName, 'wb')
    except Exception as e:
        log.logger.exception('[%s] open error cause Failed to generate test report' % fileName)
        raise e
    else:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='BPM sys自动化测试报告', description='用例执行情况如下：')
        log.logger.info('successed to generate test report [%s]' % fileName)
        return runner, fp, fileName


#
def addTc(TCpath=conf.tcPath, rule='test_*.py'):
    """

    :param TCpath: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(TCpath, rule)
    return discover


# 用BeautifulReport模块实现测试报告
def runTc(discover):
    """
    :param discover: 测试套件
    :return:
    """
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = currTime + '.html'
    try:
        result = BeautifulReport(discover)
        result.report(filename=fileName, description='测试报告', log_path=conf.reportPath)
    except Exception:
        log.logger.exception('Failed to generate test report', exc_info=True)
    else:
        log.logger.info('successed to generate test report [%s]' % fileName)
        return fileName


if __name__ == '__main__':
    test_report()
    suite = addTc(rule='test_*.py')
    runTc(suite)
