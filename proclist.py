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
def status(pid, dic={}):
    file = "/proc/"+str(pid)+"/status"
    cmd = read_cmdline("/proc/" + str(pid) + "/cmdline")
    if cmd is not 0:
        cmd = cmd[0:cmd.find("--")]
    with open(file) as status:
        beta = status.read()
    for j in beta.splitlines():
        key, value = j.split("\t")[0][0:-1], j.split("\t")[1]
        dic[key] = {"cmd":cmd, "value":value.strip()}
    return dic

for pid in psutil.pids():
    dict = status(pid)
    print(pid, dict["cmd"], dict["Name"]["value"], dict["Umask"]["value"])
