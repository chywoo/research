__author__ = 'chywoo.park'

import tizentest

sdb = tizentest.sdb
p = sdb.run("devices")
print(p.stdout.text)
p.terminate()