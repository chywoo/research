__author__ = 'chywoo.park'

import tizentest


class ABC(tizentest.TestCase):
    sdb = None
    data = "data_common"
    class_data="class_common"

    def setUp(self):
        super().setUp()
        self.sdb = tizentest.sdb

    # @tizentest.onlyPlatforms("mobile-2.3")
    def test_a(self):
        # tizentest.tizenutil.launch_mobile_vm(timeout=5)
        # tizentest.tizenutil.launch_wearable_vm(timeout=5)
        print(tizentest.tizenutil.EMULATOR_SERIAL_MOBILE)
        print(tizentest.tizenutil.EMULATOR_SERIAL_WEARABLE)
        self.assertFalse(False)

    # @tizentest.skipPlatforms("tvsdk-1.5")
    # @tizentest.onlyPlatforms("tv-2.3")
    def test_b(self):
        with self.assertRaises(TimeoutError) as ex:
            print("test")
            raise TimeoutError("Timeout")

        print("Exception: ", ex)
        self.log("Launch vm")

    def test_c(self):
        tizentest.tizenutil.start_sdb_server()

        self.sdb.run("devices")
        self.log("Shutdown")
        tizentest.tizenutil.refresh_vm_list()
        tizentest.tizenutil.shutdown_vm(name=tizentest.tizenutil.EMULATOR_NAME_MOBILE)
        tizentest.tizenutil.shutdown_vm(name=tizentest.tizenutil.EMULATOR_NAME_WEARABLE)

        self.sdb.run("devices")

        self.sdb.terminate()
        self.assertFalse(False)


    # def test_launchvm(self):
    #     util = tizentest.TizenUtil()
    #     util.launch_wearable_vm()
