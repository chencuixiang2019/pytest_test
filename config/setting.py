import os,sys
from selenium.webdriver.common.by import By
from utils.times import dt_strftime

class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @property
    def screen_path(self):
        """截图目录"""
        screenshot_dir = os.path.join(self.BASE_DIR, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return now_time, screen_file

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    # 邮件信息
    EMAIL_INFO = {
        'username': '1198422116@qq.com',  # 切换成你自己的地址
        'password': 'qizhong19921207',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '1198422116@qq.com',
    ]

cm = ConfigManager()
if __name__ == '__main__':
    print(cm.BASE_DIR)