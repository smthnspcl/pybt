import bluetooth
from sys import argv
from os.path import isdir, isfile
from os import makedirs
from atexit import register
from datetime import datetime

try:
    import simplejson as json
except ImportError:
    import json
    print "install simplejson: sudo pip install -U simplejson"


class Static(object):
    timestamp_format = "%d.%m.%Y %H:%M:%S"


class Device(object):
    timestamp = None
    address = None
    name = None
    services = None

    def __init__(self, addr, name=None):
        self.address = addr
        self.name = name
        self.services = []
        self.timestamp = datetime.now().strftime(Static.timestamp_format)

    @staticmethod
    def get_near_devices(duration=5, lookup_names=True):
        print "scanning for", duration, "seconds"
        return Device.found_to_list(bluetooth.discover_devices(duration=duration, lookup_names=lookup_names))

    def get_services(self):
        self.services = Service.found_to_list(bluetooth.find_service(address=self.address))
        return self.services

    @staticmethod
    def found_to_list(devices):
        devs = []
        for device in devices:
            devs.append(Device(device[0], device[1]))
        return devs

    def to_dict(self):
        d = self.__dict__
        for s in self.services:
            d["services"].append(s)
        return d

    def save(self, path):
        if isdir(path):
            fpath = path + self.address.replace(':', '').lower() + ".json"
            if isfile(fpath):
                fdata = json.load(open(fpath))
            else:
                fdata = {}
            fdata.update(self.to_dict())
            with open(fpath, 'w') as o:
                json.dump(fdata, o)


class Service(object):
    name = None
    protocol = None
    port = None
    description = None
    profiles = None
    service_classes = None
    provider = None
    service_id = None

    def __init__(self, service):
        self.name = service["name"]
        self.protocol = service["protocol"]
        self.port = service["port"]
        self.description = service["description"]
        self.profiles = service["profiles"]
        self.service_classes = service["service-classes"]
        self.provider = service["provider"]
        self.service_id = service["service-id"]

    @staticmethod
    def found_to_list(services):
        servs = []
        for s in services:
            servs.append(Service(s))
        return servs


class Main(object):
    _do_run = False
    out = "out/"
    duration = 5

    def ctrl_c(self):
        self._do_run = False

    @staticmethod
    def scan_until_found():
        print "scanning until found"
        devs = []
        while len(devs) == 0:
            devs = Device.get_near_devices()
        print "found", len(devs), "devices"
        return devs

    def __init__(self):
        register(self.ctrl_c)
        self.parse_args()
        self.check_args()
        self._do_run = True

    def check_args(self):
        if not isdir(self.out):
            makedirs(self.out)
            print "created directory", self.out
        if self.duration < 1 or self.duration > 20:
            print "scan duration of", str(self.duration), "seems off"

    def parse_args(self):
        i = 0
        while i < len(argv):
            if argv[i] == "-o" or argv[i] == "--out":
                self.out = argv[i + 1]
            elif argv[i] == "-d" or argv[i] == "--duration":
                self.duration = int(argv[i + 1])
            elif argv[i] == "--help":
                print "usage: python", __file__, "{arguments}"
                for ak in self.__dict__.keys():
                    if not ak.startswith('_'):
                        print "-" + ak[0], "\t", "--" + ak
                exit()
            i += 1

    def run(self):
        print "running"
        while self._do_run:
            for dev in Main.scan_until_found():
                dev.get_services()
                print "-" * 42
                print dev.address, dev.name
                print "\tservices:", len(dev.services)
                dev.save(self.out)


if __name__ == '__main__':
    Main().run()
