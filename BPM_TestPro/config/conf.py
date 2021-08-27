# 读配置文件获取项目跟目录路径 并获取所有欲使用的目录文件的路径

import os
# import sys
import sys

from test_cases.Models.Do_confini import DoingConfIni

# 获取当前路径


currPath = os.path.split(os.path.realpath(__file__))[0]
# print(currPath)
# D:\PythonProject\BPM_TestPro\config

# # 读配置文件获取项目路径
readConfig = DoingConfIni()
proPath = readConfig.getConfValue(os.path.join(currPath, 'config.ini'), 'project', 'project_path')
# D:\PythonProject
# print(proPath)
# 获取日志路径
logPath = os.path.join(proPath, 'BPM_TestPro', 'Report', 'Log')

# 测试用例路径
tcPath = os.path.join(proPath, 'BPM_TestPro', 'test_cases', 'testcases')

# 获取报告路径
reportPath = os.path.join(proPath, 'BPM_TestPro', 'Report', 'TestReport')

# 获取测试数据路径
dataPath = os.path.join(proPath, 'BPM_TestPro', 'Data')

# 保存截图路径
# 错误截图
failImagePath = os.path.join(proPath, 'BPM_TestPro', 'Report', 'Image', 'Fail')
# 成功截图
passImagePath = os.path.join(proPath, 'BPM_TestPro', 'Report', 'Image', 'Pass')
# 被调函数名称
funcName = sys._getframe().f_code.co_name
# 被调函数所在行号
funcNo = sys._getframe().f_back.f_lineno

# 被调函数所在文件名称
funcFile = sys._getframe().f_code.co_filename
