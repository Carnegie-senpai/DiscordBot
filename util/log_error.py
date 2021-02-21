import traceback
import time 

def log_error(e):
    log_file = open("shit_chan_error.txt", "a")
    log_file.write(
        "{0.tm_mon}/{0.tm_mday}/{0.tm_year} {0.tm_hour}:{0.tm_min}:{0.tm_sec}\n\n".format(time.localtime(time.time())))
    traceback.print_exc(file=log_file)
    log_file = open("shit_chan_error.txt", "a")
    log_file.write("\n\n")
    log_file.close()
