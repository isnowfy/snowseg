#snowseg

tools for chinese word segmentation and pos tagging written in python

主要是用来放置一些简单快速的中文分词和词性标注的程序

##File

* ###unigram_add_one.py
    unigram with add_one smooth
* ###unigram_good_turing.py
    unigram with good turing smooth
* ###good_turing.py
    an implement of good turing smoothing

##Usage

    >>>import unigram_add_one.py
    >>>unigram_add_one.init()
    >>>print ' '.join(list(u.solve(u'其中最简单的就是最大匹配的中文分词')))
    其中 最简单 的 就是 最大 匹配 的 中文 分词

