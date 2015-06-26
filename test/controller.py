__author__ = 'chywoo.park'

import tizentest


class ABC(tizentest.TestCase):
    @tizentest.onlyPlatform("mobile-2.3")
    def test_a(self):
        print("AAAAA")
        self.assertFalse(False)
        print("End of test")

    @tizentest.onlyPlatform("tv-2.4")
    @tizentest.skip(tizentest.intersection(tizentest.platforms, "tvsdk-1.5"))
    def test_b(self):
        print("BBBBBBB")
        self.assertFalse(False)
        print("End of test")


    # def test_launchvm(self):
    #     util = tizentest.TizenUtil()
    #     util.launch_wearable_vm()