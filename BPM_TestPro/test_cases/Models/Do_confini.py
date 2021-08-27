'''
 Code description：read conf file
 Create time：
 Developer：
'''

import logging
import configparser
from config.conf import *
from test_cases.Models.logtest import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class DoingConfIni(object):
    def __init__(self):
        """
         :param filename:
         """
        self.cf = configparser.ConfigParser()

    # 从ini文件中读数据
    def getConfValue(self, filename, section, name):
        """
         :param config:
         :param name:
         :return:
         """
        try:
            self.cf.read(filename, encoding='UTF-8')
            value = self.cf.get(section, name)
        except Exception as e:
            log.logger.exception('read file [%s] for [%s] failed , did not get the value' % (filename, section))
            raise e
        else:
            log.logger.info('read excel value [%s] successed! ' % value)
        return value

    # 向ini文件中写数据
    def writeConfValue(self, filename, section, name, value):
        """
         :param section: section
         :param name: value name
         :param value:  value
         :return: none
        """

        try:
            self.cf.add_section(section)
            self.cf.set(section, name, value)
            self.cf.write(open(filename, 'w', encoding='UTF-8'))
        except Exception:
            log.logger.exception('section %s has been exist!' % section)
            raise configparser.DuplicateSectionError(section)
        else:
            log.logger.info('write section' + section + 'with value ' + value + ' successed!')


if __name__ == '__main__':
    file_path = currPath
    print(file_path)
    read_config = DoingConfIni()
    value = read_config.getConfValue(os.path.join(currPath, 'config.ini'), 'project', 'project_path')
    print(value)
    read_config.writeConfValue(os.path.join(currPath, 'config.ini'), 'tesesection1', 'name', 'hello word')
