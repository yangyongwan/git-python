import logging
from logging.handlers import TimedRotatingFileHandler


class Mylogger(object):

    def create_logging(self):
        my_logger = logging.getLogger("my_logger")
        my_logger.setLevel('DEBUG')

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel('ERROR')
        my_logger.addHandler(stream_handler)

        log_file_hadler = TimedRotatingFileHandler(filename='log.log',when='D',interval=1,backupCount=10,encoding='utf8')
        log_file_hadler.setLevel('INFO')
        my_logger.addHandler(log_file_hadler)


        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line%(lineno)d - %(levelname)s:%(message)s]')
        stream_handler.setFormatter(formatter)
        log_file_hadler.setFormatter(formatter)

        return my_logger


if __name__ == '__main__':
    my_log_int = Mylogger()
    my_log = my_log_int.create_logging()
    my_log.info('你好info')
    my_log.debug('你好debug')
    my_log.error('你好')
    my_log.critical('好的')


































# import  logging
# from logging.handlers import TimedRotatingFileHandler
#
#
#
# my_log = logging.getLogger('A.B')
# my_log.setLevel('INFO')
#
# sh = logging.StreamHandler()
# sh.setLevel('ERROR')
# my_log.addHandler(sh)
#
#
# # fh = logging.FileHandler('logs.logs',encoding='utf8')
# fh = TimedRotatingFileHandler(filename='log.log',when= 'D',interval=1,backupCount=10,encoding='utf8')
# fh.setLevel('INFO')
# my_log.addHandler(fh)
#
#
# my_filter = logging.Filter(name='A.B')
# sh.addFilter(my_filter)
#
# formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
#
# sh.setFormatter(formatter)
# fh.setFormatter(formatter)
#
#
# a = 100
#
# my_log.debug(a)
# my_log.info('这是info等级')
# my_log.warning('这是WAENING等级')
# my_log.error('这是ERROR等级')
# my_log.critical('这是CRITICAL等级')

