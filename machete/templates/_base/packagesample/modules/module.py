# -*- coding: UTF-8 -*-
from packagesample import __version__, __chicken__, log


def main():
    log.info("hello world packagesample.modules.module v" + __version__)
    log.debug("chicken: " + str(__chicken__))
    return "hello world packagesample.modules.module v" + __version__
