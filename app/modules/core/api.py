#-*- coding: utf-8 -*-

import requests
import json


class GlobalApi():
    def __init__(self):
        pass
    
    def post(self, endpoint, dictionary):
        url = "http://23.253.71.150:8182/api/v1.0/{0}".format(endpoint)
        header = {'Content-type': 'application/json'}
        req = requests.post(url, data=json.dumps(dictionary), headers=header)


    def get_all(self, endpoint):
        url = "http://23.253.71.150:8182/api/v1.0/{0}".format(endpoint)
        header = {'Content-type': 'application/json'}
        raw = requests.get(url, headers=header).json()
        #for t in raw:
        #    if t in endpoint:
        #        print raw[t][0]
        #        foo = json.dumps(raw[t][0])
        #        return foo
        return raw
