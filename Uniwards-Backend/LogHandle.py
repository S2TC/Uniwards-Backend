"""
*   Module Name: LogHandle
*   Module Purpose: To handle all functions related to logging
"""
import datetime
from time import sleep
from ConfigHandle import Config

class Logger():
    log_name = "log.txt"
    log_file = None
    __dologging__ = False

    def __init__(self, log_name_inp):
        if (self.__dologging__ == None):
            if (Config.conf["do_we_need_logs"] == "False"):
                self.__dologging__ = False
            elif (Config.conf["do_we_need_logs"] == "True"):
                self.__dologging__ = True
            else:
                self.__dologging__ = False

        if(self.log_file == None and self.__dologging__):
            self.log_name = log_name_inp
            self.log_file = open(self.log_name, "a")
            if (self.log_file.name == self.log_name):
                print("Successfully opened Log")
            else:
                print("Error opening Log File!\nShutting Down in 5s!")
                sleep(5)
                quit()

    def Log(self, data, log_level):
        time = datetime.datetime.now()
        log_level_str = LogLevel.GetLevelStr(log_level)
        print("[%s]    -   %s  -   %s" % (log_level_str, time, data))

        if (self.__dologging__):
            if((Config.conf['DEBUG'] == "True" and log_level == LogLevel.DEBUG) or (log_level != LogLevel.DEBUG)):
                self.log_file.write("[%s]    -   %s  -   %s\n" % (log_level_str, time, data.encode("utf-8")))
                self.log_file.flush()

class LogLevel():
    DEBUG = 1
    INFO = 2
    ERROR = 3
    CRITICAL = 4

    @staticmethod
    def GetLevelStr(log_level):
        log_level_str = ""
        if (log_level == 1):
            log_level_str = "DEBUG"
        elif (log_level == 2):
            log_level_str = "INFO"
        elif (log_level == 3):
            log_level_str = "ERROR"
        elif (log_level == 4):
            log_level_str = "CRITICAL"

        return log_level_str
