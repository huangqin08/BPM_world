#! user/bin/python

'''
 Code description：auto run test case
 Create time：
 Developer：
'''

import unittest
import time
from BeautifulReport import BeautifulReport
from config.conf import *
from test_cases.Models.Testreport import test_report
from test_cases.Models.sendmessage import SendMail, getReceiverInfo

# TODO : will be use jenkins continuous intergration teachnology manage the auto project
from test_cases.Models.findnewfile import find_newest_file

if __name__ == '__main__':
    # currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    # filename = currTime + '.html'
    # # 第一种测试报告
    # test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='test_*.py')
    # result = BeautifulReport(test_suite)
    # result.report(filename=filename, description='test report', log_path=reportPath)

    # 第二种测试报告
    runner, fp, fileName = test_report()
    test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='test_*.py')
    runner.run(test_suite)
    fp.close()

    # # 查找最新的测试报告
    # file_newest = find_newest_file(reportPath)
    # print('file_newest', file_newest)
    #
    # # 发送最新的测试报告
    # readMsg = getReceiverInfo('email_receiver.txt')
    # sendmail = SendMail(readMsg)
    # sendmail.send_email(file_newest)
