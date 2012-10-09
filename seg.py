# -*- coding: UTF-8 -*-
 
import math

d = {}
log = lambda x: float('-inf') if not x else math.log(x)
prob = lambda x: d[x] if x in d else 0 if len(x)>1 else 1
 
def init(filename='SogouLabDic.dic'):
    d['_t_'] = 0.0
    with open(filename, 'r') as handle:
        for line in handle:
            word, freq = line.split('\t')[0:2]
            d['_t_'] += int(freq)+1
            try:
                d[word.decode('gbk')] = int(freq)+1
            except:
                d[word] = int(freq)+1
 
def solve(s):
    l = len(s)
    p = [0 for i in range(l+1)]
    t = [0 for i in range(l)]
    for i in xrange(l-1, -1, -1):
        p[i], t[i] = max((log(prob(s[i:i+k])/d['_t_'])+p[i+k], k)
                        for k in xrange(1, l-i+1))
    while p[l]<l:
        yield s[p[l]:p[l]+t[p[l]]]
        p[l] += t[p[l]]
 
if __name__ == '__main__':
    init()
    s = u'其中最123简单的就是最大匹配的中文分词'
    print ' '.join(list(solve(s)))
