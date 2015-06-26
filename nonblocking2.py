__author__ = 'chywoo.park'
from subprocess import Popen, PIPE
from threading import Thread
from queue import Queue, Empty

CMD = ["/Users/chywoo.park/tizen23/tools/sdb", "devices"]

stdout_fp = open("stdout.txt", "w")
stderr_fp = open("stderr.txt", "w")
p = Popen(CMD, stdout=PIPE, stderr=PIPE)

print("Object: ", p)
print("")
eof = False


stdout, err = p.communicate(timeout=10)


while not eof:
    data = stdout.read()
    # data, err = p.communicate(timeout=10)

    if data == b'':
        print("EOF")
        eof = True

    print(data.decode('utf-8'))

