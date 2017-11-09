import logging

def LogIntoFile(self, logname, loggerfile=None):

     logger = logging.getLogger(logname)
     logger.setLevel(logging.WARNING)

     # 创建一个handler，输出到log文件
     fh = logging.FileHandler(loggerfile)
     fh.setLevel(logging.DEBUG)
     formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
     fh.setFormatter(formatter)
     logger.addHandler(fh)
     return logger

def LogIntoConsole(self, logname):

    logger = logging.getLogger(logname)
    logger.setLevel(logging.WARNING)

    # 创建一个handler，输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger



