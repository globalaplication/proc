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

def status(pid, dic={}):
    file = "/proc/"+str(pid)+"/status"
    with open(file) as status:
        beta = status.read()
    for j in beta.splitlines():
        key, value = j.split("\t")[0][0:-1], j.split("\t")[1]
        dic[key] = {"value":value.strip()}
    return dic

print (status(1))
