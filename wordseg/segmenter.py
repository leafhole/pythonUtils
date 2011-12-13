#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re
import libwordbreak

class segmenter(object):
    '''
    GBK word segmenter
    '''

    def __init__(self, dictpath=os.sep.join((os.path.dirname(os.path.realpath(__file__)), '..'))):
        libwordbreak.cut_load(dictpath)
        self.__sep = re.compile(" ")

    def __del__(self):
        libwordbreak.cut_unload()
        del self.__sep

    def seg(self, word):
        res = libwordbreak.word_break(word)
        return self.__sep.split(res)

    def seg_all(self, word):
        res = libwordbreak.word_break_all(word)
        return self.__sep.split(res)

    def seg_property(self, word, property):
        res = libwordbreak.word_break_property(word, property)
        return self.__sep.split(res)

    def seg_all_property(self, word, property):
        res = libwordbreak.word_break_all_property(word, property)
        return self.__sep.split(res)

    def seg_single(self, word):
        res = libwordbreak.word_break_single(word)
        return self.__sep.split(res)

