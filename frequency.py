# -*- coding: utf-8 -*-

class BaseProb(object):
    
    def __init__(self):
        self.d = {}
        self.total = 0
        self.d['_none_'] = 0

    def exists(self, key):
        return key in self.d

    def getsum(self):
        return self.total

    def get(self, key):
        if not self.exists(key):
            return False, d['_none_']
        return True, d[key]


class AddOneProb(BaseProb):

    def __init__(self):
        self.d = {}
        self.total = 0
        self.d['_none_'] = 1

    def add(self, key, value):
        self.total += value+1
        if not self.exists(key):
            d[key] = 0
        else:
            d[key] += value+1
