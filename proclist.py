import psutil

print (psutil.pids())

import os

pid = [pid for pid in os.listdir("/proc") if pid.isdigit()]

def read_cmdline(file):
    with open(file) as read:
        beta = read.read()
    if len(beta) is 0:
        return 0
    else:
        return beta

for j in pid:
    cmd = read_cmdline("/proc/" + str(j) + "/cmdline")
    if cmd is not 0:
        print (cmd[0:cmd.find("--")], j)
