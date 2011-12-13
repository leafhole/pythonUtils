#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from segmenter import segmenter

def test(word):
    seg = segmenter("..")
    s = word.decode("utf8").encode("gbk")
    t = seg.seg(s)
    for tt in t:
        print tt.decode("gbk").encode("utf8")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        test(sys.argv[1])
