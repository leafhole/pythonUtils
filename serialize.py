# -*- coding:utf8 -*-

import sys
import traceback
import cPickle

class serializer(object):
    '''
    Util: serializer.
    '''

    @staticmethod
    def open_file(fname, mode='r'):
        fp = None
        try:
            fp = open(fname, mode)
        except:
            print traceback.print_exc()
            sys.exc_clear()
        return fp

    @staticmethod
    def dump(obj, fname):
        fp = serializer.open_file(fname, 'wb+')
        if fp is None:
            return Fasle
        ret = True
        try:
            cPickle.dump(obj, fp, protocol=2)
        except:
            print traceback.print_exc()
            sys.exc_clear()
            ret = False
        fp.close()
        return ret

    @staticmethod
    def load(fname):
        obj = None
        fp = serializer.open_file(fname, 'rb')
        if fp is None:
            return obj
        try:
            obj = cPickle.load(fp)
        except:
            print traceback.print_exc()
            sys.exc_clear()
        fp.close()
        return obj


