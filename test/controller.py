__author__ = 'chywoo.park'

import tizentest


class ABC(tizentest.TestCase):
    sdb = None
    data = "data_common"
    class_data="class_common"

    def setUp(self):
        self.sdb = tizentest.sdb

    # @tizentest.onlyPlatforms("mobile-2.3")
    # def test_a(self):
    #     self.assertFalse(False)

    # @tizentest.skipPlatforms("tvsdk-1.5")
    # @tizentest.onlyPlatforms("tv-2.3")
    def test_b(self):
        self.log("*"*80)
        self.log("Launch vm")
        p = tizentest.tizenutil.launch_mobile_vm()
        self.log(p)
        self.assertEqual(0, p)

    def test_c(self):
        self.log("*"*80)
        tizentest.tizenutil.start_sdb_server()

        self.sdb.run("devices")
        self.log("Shutdown")
        tizentest.tizenutil.shutdown_vm(name=tizentest.EMULATOR_NAME_MOBILE)

        self.sdb.run("devices")

        self.sdb.terminate()
        self.assertFalse(False)


    # def test_launchvm(self):
    #     util = tizentest.TizenUtil()
    #     util.launch_wearable_vm()
