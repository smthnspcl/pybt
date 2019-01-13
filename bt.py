from sys import argv
from os.path import isdir
from os import makedirs
from atexit import register

from libs.Static import Static
from libs.bt.classic import ClassicDevice
from libs.bt.le import LEDevice
from libs.bt.beacon import Beacon


class Scanner(object):
    _do_run = False
    out = "out/"
    duration = 5

    def ctrl_c(self):
        self._do_run = False

    @staticmethod
    def scan_until_found():
        print("scanning until found")
        devs = []
        while len(devs) == 0:
            print("classic")
            devs += ClassicDevice.scan()
            print("le")
            devs += LEDevice.scan(read_all=True)
            print("beacon")
            devs += Beacon.scan()
        print("found", len(devs), "devices")
        return devs

    def __init__(self):
        register(self.ctrl_c)
        self.parse_args()
        self.check_args()
        self._do_run = True

    def check_args(self):
        if not isdir(self.out):
            makedirs(self.out)
            print("created directory", self.out)
        if self.duration < 1 or self.duration > 20:
            print("scan duration of", str(self.duration), "seems off")

    def parse_args(self):
        i = 0
        while i < len(argv):
            if argv[i] == "-o" or argv[i] == "--out":
                self.out = argv[i + 1]
            elif argv[i] == "-d" or argv[i] == "--duration":
                self.duration = int(argv[i + 1])
            elif argv[i] == "--help":
                print("usage: python", __file__, "{arguments}")
                for ak in self.__dict__.keys():
                    if not ak.startswith('_'):
                        print("-" + ak[0], "\t", "--" + ak)
                exit()
            i += 1

    def run(self):
        print("running")
        while self._do_run:
            for dev in self.scan_until_found():
                if isinstance(dev, ClassicDevice):
                    dev.get_services()
                    print("-" * 42)
                    print("classic", dev.address, dev.name)
                    print("\tservices:", len(dev.services))
                if isinstance(dev, Beacon):
                    print("-" * 42)
                    print("beacon", dev.address, dev.power, dev.rssi)
                if isinstance(dev, LEDevice):
                    print("-" * 42)
                    print("le", dev.address, dev.name)
                    print("\tservices:", len(dev.services), "\tads:", len(dev.advertisements))
                Static.save(dev, self.out)


if __name__ == '__main__':
    Scanner().run()
