import os
import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import conf
from test_cases.Models.logtest import Logger

log = Logger(__name__)


class SendMail(object):
    '''
     邮件配置信息
     '''

    def __init__(self, receiver, subject='BPM系统测试报告--来自老婆的信', server='smtp.qq.com', fromuser='549418724@qq.com',
                 frompassword='lkgvptfualbkbccc', sender='549418724@qq.com'):
        """
        :param receiver:
         :param subject:
         :param server:
         :param fromuser:
         :param frompassword:
         :param sender:
         """

        self._server = server
        self._fromuser = fromuser
        self._frompassword = frompassword
        self._sender = sender
        self._receiver = receiver
        self._subject = subject

    def send_email(self, fileName):
        # # 邮件服务器
        # smtpserver = 'smtp.qq.com'
        # # 发件人
        # sender = '549418724@qq.com'
        # # 发件人授权码
        # sender_AuthCode = 'lkgvptfualbkbccc'
        # # 收件人
        # receiver = ['570219494@qq.com', 'huangqin@guojingold.com']

        #   打开报告文件读取文件内容
        try:
            f = open(os.path.join(conf.reportPath, fileName), 'rb')
            fileMsg = f.read()
        except Exception:
            log.logger.exception(
                'open or read file [%s] failed,No such file or directory: %s' % (fileName, conf.reportPath))
            log.logger.info('open and read file [%s] successed!' % fileName)
        else:
            f.close()

        #   邮件主题
        subject = 'Python test send email--来自老婆的信'

        # 邮件正文
        body = MIMEText(fileMsg, 'html', 'utf-8')

        # 邮件对象
        email = MIMEMultipart()
        email['Subject'] = Header(subject, 'utf-8').encode()
        email['From'] = self._sender
        email['To'] = ','.join(self._receiver)
        email['date'] = time.strftime('%Y-%m-%d %H_%M_%S')
        email.attach(body)

        # 附件
        att = MIMEText(fileMsg, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="test_report.html"'
        # print(att)
        email.attach(att)

        # 发送邮件
        try:
            smtp = smtplib.SMTP_SSL(self._server, 465)
            smtp.login(self._sender, self._frompassword)
        except Exception as e:
            log.logger.exception('connect [%s] server failed or username and password incorrect!' % smtp)
            raise e
        else:
            log.logger.info('email server [%s] login success!' % smtp)
            try:
                smtp.sendmail(self._sender, self._receiver, email.as_string())
            except Exception as e:
                log.logger.exception('send email failed!')
                raise e
            else:
                log.logger.info('send email successed!')
        smtp.quit()


#   从文件中读取邮件接收人信息
def getReceiverInfo(fileName):
    '''
    :param filename: 读取接收邮件人信息
    :return: 接收邮件人信息
    '''
    try:
        openFile = open(os.path.join(conf.dataPath, fileName))
    except Exception:
        log.logger.exception(
            'open or read file [%s] failed,No such file or directory: %s' % (fileName, conf.dataPath))
    else:
        log.logger.info('open file [%s] successed!' % fileName)
        for line in openFile:
            msg = [i.strip() for i in line.split(',')]
            log.logger.info('reading [%s] and got receiver value is [%s]' % (fileName, msg))
            return msg


if __name__ == '__main__':
    readMsg = getReceiverInfo('email_receiver.txt')
    sendmail = SendMail(readMsg)
    # sendmail.send_email()
