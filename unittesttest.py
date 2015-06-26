__author__ = 'chywoo.park'

import tizentest

class ABC(unittest.TestCase):
    @unittest.skip("aaa")
    def test_a(self):
        print("AAAAA")
        self.assertFalse(False)
        print("End of test")

    @
    def test_mobileprofile(self):
        print("Mobile")
        self.assertFalse(False)


