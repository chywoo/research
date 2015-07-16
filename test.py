import re
import test


class AttrTest:
    data = 'List of devices attached\nemulator-26111        device      wearable\nemulator-26101        device      mobile\n'

    def refresh(self):
        p = re.compile("^emulator-\d+\s+device\s+\w+$", re.MULTILINE)
        p2 = re.compile("\s+device\s+")

        for i in p.findall(self.data):
            print(i)
            l = p2.split(i)
            print(l)
            name = str(l[1])

            setattr(self, "EMUL_" + name.upper(), name)
            setattr(self, "EMUL_SERIAL_" + name.upper(), l[0])



test = AttrTest()
test.refresh()
print(test.EMUL_MOBILE)
print(test.EMUL_WEARABLE)
print(test.EMUL_SERIAL_MOBILE)
