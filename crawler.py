#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import re
import sys
import urllib2
import traceback
import logging
from logger import init_logger
from config import config_parser


class basic_crawler(object):
    '''
    simplest single-thread crawler
    '''

    def __init__(self, cfgpath=None):
        self.__load_config(cfgpath)
        self.__init_data()
        self.__prepare()

    def __del__(self):
        self.__finish_data()

    def __str__(self):
        return self.__class__.__name__

    def __load_config(self, cfgpath):
        self.__base_dir = os.path.dirname(os.path.realpath(__file__))
        cfgfile = cfgpath
        if cfgfile is None:
            cfgfile = os.sep.join((self.__base_dir, "conf", "crawler.ini"))
        self.__cfgparser = config_parser(cfgfile)
        proxy = self.__cfgparser.get("CRAWL_SETTING", "proxy", "")
        self.__proxy = proxy.strip(" \t\n")
        self.__data_dir = self.__cfgparser.get("DEPLOY_INFO", "data_path", os.sep.join((self.__base_dir, "data")))
        self.__log_dir = self.__cfgparser.get("DEPLOY_INFO", "log_path", os.sep.join((self.__base_dir, "log")))
        os.system("mkdir -p %s %s" % (self.__data_dir, self.__log_dir))

    def __init_data(self):
        self.__logger = init_logger("%s" % self.__class__.__name__, os.sep.join((self.__log_dir, "CRAWL.log")))
        self.__http = re.compile(r'http(s)?://', re.I)

    def __finish_data(self):
        del self.__logger
        del self.__http

    def __prepare(self):
        if self.__proxy is not None and len(self.__proxy) > 0:
            if self.__http.match(self.__proxy) is None:
                self.__proxy = "http://" + self.__proxy
            opener = urllib2.build_opener(urllib2.ProxyHandler({'http':self.__proxy}))
            urllib2.install_opener(opener)
            self.__logger.debug("STE Proxy: %s" % self.__proxy)
        self.__logger.debug("Prepare done!\n")

    def crawl(self, url, max_retry=5):
        self.__logger.debug("Crawling %s ... ..." % url)
        body = None
        retry = 0
        while retry < max_retry:
            try:
                response = urllib2.urlopen(url)
                body = response.read()
                break
            except:
                self.__logger.warn("Exception occurs crawling: %s" % url)
                retry += 1
                time.sleep(retry)
        return body

