__author__ = 'chywoo.park'
from subprocess import Popen, PIPE
from threading import Thread
from queue import Queue, Empty

CMD = ["/Users/chywoo.park/tizen23/tools/sdb", "devices"]

stdout_fp = open("stdout.txt", "w")
stderr_fp = open("stderr.txt", "w")
p = Popen(CMD, stdout=stdout_fp, stderr=stderr_fp)

print("Object: ", p)
print("")
eof = False
print("Wait: ", p.wait())
# while not eof:
#     v = p.poll()
#     print("Poll: ", v)
#     data = p.stdout.read()
#     # data, err = p.communicate(timeout=10)
#
#     if data == b'':
#         print("EOF")
#         eof = True
#
#     print(data.decode('utf-8'))


stdout_fp.close()
stderr_fp.close()

with open("stdout.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)

with open("stderr.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)
