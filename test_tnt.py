# -*- coding: utf-8 -*-

import codecs

import tnt

def getdata(filename='brown.txt'):
    data = []
    f = codecs.open(filename, 'r', 'utf-8')
    for line in f:
        line = line.strip()
        if not line:
            continue
        words = map(lambda x: x.split('/'), line.split(' '))
        data.append(words)
    return data

def main():
    data = getdata()
    model = tnt.TnT()
    model.train(data)
    ret = [model.tag(map(lambda x:x[0], sent)) for sent in data]
    total = 0
    error = 0
    for c1, sent in enumerate(data):
        for c2, wd in enumerate(sent):
            total += 1
            if wd[1] != ret[c1][c2][1]:
                error += 1
    print 'total: %d, error: %d, precision: %f' %\
        (total, error, float(total-error)/total)

if __name__ == '__main__':
    main()
