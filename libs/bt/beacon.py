from bluetooth.ble import BeaconService


class Beacon(object):
    uuid = None
    major = None
    minor = None
    power = None
    rssi = None
    address = None

    def __init__(self, data, address):
        self.uuid = data[0]
        self.major = data[1]
        self.minor = data[2]
        self.power = data[3]
        self.rssi = data[4]
        self.address = address

    @staticmethod
    def scan():
        return Beacon.found_to_list(BeaconService().scan(2))

    @staticmethod
    def found_to_list(beacons):
        b = []
        for a, d in list(beacons.items()):
            b.append(Beacon(d, a))
        return b
