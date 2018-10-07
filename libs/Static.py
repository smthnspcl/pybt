from os.path import isfile, isdir
import json
from datetime import datetime
import pprint

class Static(object):
    timestamp_format = "%d.%m.%Y %H:%M:%S"

    @staticmethod
    def make_timestamp():
        return datetime.now().strftime(Static.timestamp_format)

    @staticmethod
    def save(obj, path):
        if isdir(path):
            fpath = path + obj.address.replace(':', '').lower() + ".json"
            print fpath
            if isfile(fpath):
                fdata = json.load(open(fpath))
            else:
                fdata = {}
            fdata.update(obj.to_dict())
            pprint.pprint(fdata)
            with open(fpath, 'w') as o:
                json.dump(fdata, o)
