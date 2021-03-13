import time
import datetime

def dt_strftime(fmt="%Y%m"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)

def timestamp():
    """时间戳"""
    return time.time()
