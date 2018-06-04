#!/usr/bin/python3.5.3
# -*-coding:UTF-8-*-

from logging.config import fileConfig
import logging
import os


class log:
    """python logger util"""

    __path = os.path.split(os.path.realpath(__file__))[0]
    fileConfig(__path + '/logger.ini')

    __logger = logging.getLogger()

    def __init__(self, name):
        self.__logger = logging.getLogger(name)
        return

    def debug(self, msg):
        self.__logger.debug(msg)
        return

    def info(self, msg):
        self.__logger.info(msg)
        return

    def warning(self, msg):
        self.__logger.warning(msg)
        return

    def error(self, msg):
        self.__logger.error(msg)
        return

    def critical(self, msg):
        self.__logger.critical(msg)
        return
