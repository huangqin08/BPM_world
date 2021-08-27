import logging
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from selenium import webdriver
from Page_object.login_page import LoginPage
from Page_object.officeSupplies import OfficeSupplies
from Page_object.consignmentsales import ConsignmentSales
from ddt import ddt, data, unpack

from base.base import testLoginData
from test_cases.Models.findnewfile import find_newest_file
# from test_cases.Models.sendmessage import send_email
from test_cases.Models.logtest import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
unpwData = [testLoginData.readExcel(1, 1), testLoginData.readExcel(1, 2)]


@ddt
class Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 加载driver驱动，使得newChromeDriver()对象能正常被调用
        # 获取chrome驱动并正确打开浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        log.logger.info('opened the browser successed!')

    def setUp(self) -> None:
        self.lp = LoginPage(self.driver)
        self.ospage = OfficeSupplies(self.driver)
        self.cost = ConsignmentSales(self.driver)
        log.logger.info('************************starting run test cases************************')

    # @data(unpwData)
    @data(['009410', '000000'])
    @unpack
    def test_01(self, user, pwd):
        # print('user', user)
        # print(pwd)
        # 登录流程
        # user = '009410'
        # pwd = '000000'
        # self.lp.login(kwargs['user'], kwargs['pwd'])
        self.lp.login(user, pwd)
        title = self.driver.title
        self.assertIn(u"国金黄金首页", title, msg='断言失败')

    @unittest.skip("跳过")
    @data('笔')
    def test_02(self, txt):
        # # 办公用品领用流程
        # sreachstr = '笔'
        # # self.ospage.office_supplies(kwargs['sreachstr'])
        self.ospage.office_supplies(txt)

    @unittest.skip("跳过")
    def test_03(self):
        # 费用报销流程
        numbercount = '1'  # 发票张数
        reqfuture1 = '出差报销差旅费用'  # 费用事由
        self.cost.Consignment(numbercount, reqfuture1)
        title = self.driver.title
        self.assertEqual(title, u"申请记录", msg='断言失败')

    def tearDown(self):
        """
        :return:
         """
        self.driver.refresh()
        log.logger.info('************************test case run completed************************')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        log.logger.info('quit the browser success!')


if __name__ == '__main__':
    unittest.main()
