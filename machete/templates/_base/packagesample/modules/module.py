# -*- coding: UTF-8 -*-
from packagesample import __version__
# from packagesample import __chicken__
from packagesample import log
import __builtin__


def main():
    log.info("hello world packagesample.modules.module v" + __version__)
    log.debug("chicken: " + str(__builtin__.chicken))
    return "hello world packagesample.modules.module v" + __version__
