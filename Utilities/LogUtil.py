import logging
import time


class Logger:
    def __init__(self,logger,file_leve=logging.INFO):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt=logging.Formatter("%(asctime)s--%(filename)s--%(message)s")
        cur_time=time.strftime("%Y-%m-%d")
        self.filename="..//Log//logging"+ cur_time+".txt"
        fh=logging.FileHandler(self.filename,mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_leve)

        self.logger.addHandler(fh)

