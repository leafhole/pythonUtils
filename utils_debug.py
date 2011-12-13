#!/usr/bin/env python
#coding=utf-8


import sys,time
import _ctypes
import hashlib

ISOTIMEFORMAT='%Y-%m-%d %X'
ISODATEFORMAT='%Y-%m-%d'

def FUNCTION_NAME():
    codename = sys._getframe(1).f_code
    return codename.co_name,codename.co_varnames
    pass # the end of FUNCTION_NAME
def LINENO():
    codename = sys._getframe(1)
    return codename.f_lineno
    pass # the end of LINENO() 
def NOW():
    return time.strftime(ISOTIMEFORMAT,time.localtime())
    pass # the end of NOW        

def timestamp():
    lt = time.localtime(time.time())
    return "%04d-%02d-%02d %02d:%02d:%02d" % (lt[0], lt[1], lt[2], lt[3], lt[4], lt[5])

def BEAUTIFUL_SPLIT_LINE():
    sp =  "$$$$$$$$$####################$$$$$$$$$$"
    print sp
    return sp
    pass

def di(obj_id):
    return _ctypes.PyObj_FromPtr(obj_id)

def get_md5(line):# calulate the md5 of the input line .
    m = hashlib.md5()
    m.update( line )
    return m.hexdigest() 

def safe_int(text):
    ret_int=0;
    try:
        text = text.strip();
        ret_float = float(text);
        ret_int = int(ret_float)
    except:
        pass
    return ret_int;
		
    

def LOOKOUT(input_string = ""):
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    for i in range(5):
        print input_string;
        pass
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    pass
