#!/usr/bin/env python
#encoding=utf8
# mysqlTable.py --- 
# 
# Filename: mysqlTable.py
# Description: 
# Author: su yedong
# Maintainer: 
# Created: 3 03 21 14:16:26 2012 (+0800)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# URL: 
# Keywords: 
# Compatibility: 
# 
# 

# Commentary: 
# 
# 
# 
# 

# Change Log:
# 
# 
# 
# 
# If you have any problem with this program , please feel free to contact
#      mail: suyd@kuxun.cn
#      gtalk: rtemslinux@gmail.com
#      msn:  suyedong@hotmail.com
#   
# 
# 

# Code:
from utils_mysql import dbConn


class MySQLTable(object):
    """
    """
    
    def __init__(self, ):
        """
        """
        self.__cursor = None
        self.__connection = None

        self.dbConf = None
        pass

    def setDbConf(self, dbConf):
        """
        """
        self.dbConf = dbConf
        pass
        
    def connect(self, dbConf = None):
        """
        """
        if dbConf is None:
            self.__connection, self.__cursor = dbConn(self.dbConf)
            pass
        else:
            self.__connection, self.__cursor = dbConn(dbConf)
            pass
        pass

    def executeSql(self, sql):
        """
        """
        ret = self.__cursor.execute(sql)
        return ret
        pass

    def fetchAll(self, ):
        """
        """
        ret = self.__cursor.fetchall()
        return ret
        pass

    def fetchOne(self, ):
        """
        """
        ret = self.__cursor.fetchone()
        return ret

    def commit(self, ):
        """
        """
        self.__connection.commit()
        pass

    
# 
# mysqlTable.py ends here
