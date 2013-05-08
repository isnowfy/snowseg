# -*- coding: utf-8 -*-

import good_turing

class BaseProb(object):
    
    def __init__(self):
        self.d = {}
        self.total = 0.0
        self.d['_none_'] = 0

    def exists(self, key):
        return key in self.d

    def getsum(self):
        return self.total

    def get(self, key):
        if not self.exists(key):
            return False, self.d['_none_']
        return True, self.d[key]


class AddOneProb(BaseProb):

    def __init__(self):
        self.d = {}
        self.total = 0.0
        self.d['_none_'] = 1

    def add(self, key, value):
        self.total += value+1
        if not self.exists(key):
            self.d[key] = 0
        self.d[key] += value+1


class GoodTuringProb(BaseProb):

    def __init__(self):
        self.d = {}
        self.total = 0.0
        self.handled = False

    def add(self, key, value):
        if not self.exists(key):
            self.d[key] = 0
        self.d[key] += value

    def get(self, key):
        if not self.handled:
            self.handled = True
            tmp, self.d = good_turing.main(self.d)
            self.d['_none_'] = tmp
            self.total = sum(self.d.values())+0.0
        if not self.exists(key):
            return False, self.d['_none_']
        return True, self.d[key]
