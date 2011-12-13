# /usr/bin/env python
# coding=utf8
# utils_mysql.py --- 
# 
# Filename: utils_mysql.py
# Description: 
# Author: suyd
# Maintainer: 
# Created: 日  6月 27 11:11:53 2010 (+0800)
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
import MySQLdb
from unilog import unilogger

def dbcon(host,name,user,password,port_num=3306):
    #print "connectiong2 ", host,   user,   password,port_num
    unilogger.info('connect mysql://%s:%s@%s:%d/%s' % (user,'*'*len(password),host,port_num,name))
    db  = MySQLdb.connect(host=host,   user=user,   passwd=password,   db=name,charset="utf8",port=port_num)
    cur = db.cursor()
    return db,cur

def dbConn(dbConf):
    host = dbConf.get("host")
    name = dbConf.get("name")
    user = dbConf.get("user")
    password = dbConf.get("password")
    port_num = dbConf.get("port",3306)
    return dbcon(host,name,user,password,port_num)

# 
# utils_mysql.py ends here
