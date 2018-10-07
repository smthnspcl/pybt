from scapy.all import *
from sys import argv
from os import system, geteuid

from libs.oui import OuiEntries


class Arguments(object):
    interface = None

    def __init__(self, **kwargs):
        self.interface = kwargs.get("interface")

    @staticmethod
    def parse(argv):
        i = 0
        a = Arguments()
        while i < len(argv):
            if argv[i] in ["-i", "--interface"]:
                a.interface = argv[ i + 1]
            i += 1
        return a


def set_promiscuous(iface, start=True):
    do = "start"
    if not start:
        do = "stop"
    system("sudo airmon-ng %s %s" % (do, iface))
    return iface + "mon"


def get_essid(dot11elt):
    if dot11elt.ID == 0:
        ssid = repr(dot11elt.info)
        if ssid[:2] in ['b"', "b'"]:
            ssid = ssid[1:]
        return ssid
    return ""


def send_probe_reqs(infile):
    with open(infile) as i:
        for l in i:
            print l  # todo


def pkt_summery_1line(pkt):
    if Dot11 in pkt:
        lua = []
        for a in [pkt.addr1, pkt.addr2, pkt.addr3, pkt.addr4]:
            if a is not None and a != "ff:ff:ff:ff:ff:ff":
                lua.append(a.upper())
        for s in o.lookup_multiple(lua):
            print s.address, s.entry.company
        print pkt.addr2, ">>", pkt.addr1
        for t in [Dot11Beacon, Dot11ProbeReq, Dot11ProbeResp, Dot11Auth, Dot11Disas, Dot11Deauth,
                  Dot11Elt]:
            if t in pkt:
                l = pkt.getlayer(t)
                print l.name
                if t is Dot11Elt:
                    get_essid(l)


def main(a):
    o = OuiEntries()

    def cb(x):
        pkt_summery_1line(x)

    sniff(iface=a.interface, prn=cb)


if __name__ == '__main__':
    if geteuid() != 0:
        print "run with root"
        exit()
    a = Arguments.parse(argv)
    if not a.interface.endswith('mon'):
        a.interface = set_promiscuous(a.interface)
    try:
        main(a)
    except KeyboardInterrupt:
        pass
    a.interface = set_promiscuous(a.interface, False)
