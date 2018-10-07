from ..Device import Device
from bluepy.btle import Scanner, DefaultDelegate, Peripheral, BTLEException


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            pass
        if isNewData:
            pass


class Advertisement(object):
    ad_type = None
    description = None
    value = None

    def __init__(self, **kwargs):
        if "ad_type" in kwargs.keys():
            self.ad_type = kwargs.get("ad_type")
        if "description" in kwargs.keys():
            self.description = kwargs.get("description")
        if "desc" in kwargs.keys():
            self.description = kwargs.get("desc")
        if "val" in kwargs.keys():
            self.value = kwargs.get("val")
        if "value" in kwargs.keys():
            self.value = kwargs.get("value")


class Service(object):
    uuid = None
    characteristics = None

    def __init__(self, **kwargs):
        if "uuid" in kwargs.keys():
            self.uuid = kwargs.get("uuid")
        if "characteristics" in kwargs.keys():
            self.characteristics = kwargs.get("characteristics")

    @staticmethod
    def from_device(address, addrType):
        services = []
        try:
            device = Peripheral(address, addrType)
        except BTLEException:
            return []
        for s in device.getServices():
            services += Service(
                uuid=s.uuid,
                characteristics=Characteristic.from_service(s)
            )
        return services


class Characteristic(object):
    supportsRead = False
    handle = None
    uuid = None
    properties = None
    data = None

    def __init__(self, **kwargs):
        if "supportsRead" in kwargs.keys():
            self.supportsRead = kwargs.get("supportsRead")
        if "handle" in kwargs.keys():
            self.handle = kwargs.get("handle")
        if "uuid" in kwargs.keys():
            self.uuid = kwargs.get("uuid")
        if "properties" in kwargs.keys():
            self.properties = kwargs.get("properties")
        if "data" in kwargs.keys():
            self.data = kwargs.get("properties")

    @staticmethod
    def from_service(service):
        chars = []
        for c in service.getCharacteristics():
            chars += Characteristic(
                supportsRead=c.supportsRead(),
                data=c.read(),
                properties=c.properties,
                uuid=c.uuid,
                handle=c.getHandle()
            )


class LEDevice(Device):
    name = None
    addressType = None
    rssi = None
    connectable = False
    advertisements = None
    services = None

    def __init__(self, address, name=""):
        Device.__init__(self, address)
        self.name = name
        self.advertisements = []
        self.services = []

    @staticmethod
    def found_to_list(devices):
        devs = []
        for d in devices:
            _ = LEDevice(d.addr)
            _.addressType = d.addrType
            _.rssi = d.rssi
            _.connectable = d.connectable
            for (at, d, v) in d.getScanData():
                if d == "Complete Local Name" or d == "Short Local Name":
                    _.name = v
                _.advertisements.append(Advertisement(
                    ad_type=at, desc=d, val=v
                ))
            _.services = Service.from_device(_.address, _.addressType)
            devs.append(_)
        return devs

    @staticmethod
    def scan(duration=3.0):
        s = Scanner().withDelegate(ScanDelegate())
        return LEDevice.found_to_list(s.scan(duration))

    def to_dict(self):
        ads = []
        for a in self.advertisements:
            ads.append(a.__dict__)
        d = self.__dict__
        d["advertisements"] = ads
        return d
