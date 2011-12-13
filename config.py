# -*- coding: utf8 -*-

import sys
import ConfigParser

class config_parser(object):
    '''
    config parser wrapper
    '''

    def __init__(self, cfgpath):
        self.__parser = self.__load_config(cfgpath)

    def __del__(self):
        del self.__parser

    def __load_config(self, cfgpath):
        try:
            cfg = ConfigParser.RawConfigParser()
            cfg.read(cfgpath)
            return cfg
        except:
            sys.exc_clear()
            return None

    def get(self, section, key, defval=None):
        try:
            ret = self.__parser.get(section, key)
            return ret
        except:
            sys.exc_clear()
            return defval


