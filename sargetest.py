__author__ = 'chywoo.park'

import sarge
import logging

logging.basicConfig(level=logging.DEBUG)

stdo = sarge.Capture()
stde = sarge.Capture()
pipe = sarge.Pipeline(source="/Users/chywoo.park/tizen23/tools/sdb devices",
                      stdout=stdo, stderr=stde, mode=sarge.Command.MODE_FILE, close_fds=True)

p = pipe.run()


out = p.stdout
eof = False

while not eof:
    data = out.readline()

    if data == b'':
        eof = True
        break
    print(data.decode("utf-8"))

print("Closing")
out.close()
pipe.close()
