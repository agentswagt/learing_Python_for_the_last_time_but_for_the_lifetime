import os
from time import gmtime, strftime
import sys
current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(current_time)

while True:
    log_text = raw_input("Log: ")
    if log_text == "":
        sys.exit()
    final_log_text = """
    [TIME:{}]->{}\n""".format(current_time, log_text)
    with open("log.txt", "a") as f:
        f.write(final_log_text)
        f.close()
    

