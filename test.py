__author__ = 'chywoo.park'
import psutil

for i in psutil.process_iter():
    print(i.name())
    # cmd = i.cmdline()
    # if cmd == ['sdb', 'fork-server', 'server']:
    #     print("Found")

