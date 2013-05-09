# -*- coding: utf-8 -*-

'''
Implementation of 'TnT - A Statisical Part of Speech Tagger'
'''

import frequency

class TnT(object):

    def __init__(self, N=1000):
        self.N = 1000
        self.l1 = 0.0
        self.l2 = 0.0
        self.l3 = 0.0
        self.status = {'BOS', 'EOS'}
        self.wd = frequency.AddOneProb()
        self.uni = frequency.AddOneProb()
        self.bi = frequency.AddOneProb()
        self.tri = frequency.AddOneProb()
        self.eos = frequency.AddOneProb()

    def train(self, data):
        now = ['BOS', 'BOS']
        for sentence in data:
            for word, tag in sentence:
                now.append(tag)
                self.status.add(tag)
                self.wd.add((tag, word), 1)
                self.uni.add(tag, 1)
                self.bi.add(tuple(now[1:]), 1)
                self.tri.add(tuple(now), 1)
                now.pop(0)
            self.eos.add(now[-1], 1)
        tl1 = 0.0
        tl2 = 0.0
        tl3 = 0.0
        for now in self.tri.samples():
            pass
