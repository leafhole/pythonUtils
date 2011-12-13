#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import traceback

import MySQLdb
import _mysql_exceptions


class mysql_basic_operator(object):
    '''
    basic mysql operator
    '''

    def __init__(self):
        self.__cxn = None
        self.__cur = None

    def __del__(self):
        if self.__cxn is not None:
            self.__cxn.close()
        del self.__cur
        del self.__cxn

    def connect_mysql(self, host, user, passwd, db, port, charset):
        try:
            self.__cxn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, port=port, charset=charset)
            self.__cur = self.__cxn.cursor()
            return True
        except:
            print traceback.print_exc()
            self.__cxn, self.__cur = None, None
            sys.exc_clear()
            return False

    def execute(self, cmd):
        try:
            self.__cur.execute(cmd)
            return self.__cur.fetchall()
        except:
            print traceback.print_exc()
            sys.exc_clear()
            return None

    def commit(self):
        try:
            self.__cxn.commit()
            return True
        except:
            print traceback.print_exc()
            sys.exc_clear()
            return False

