# -*- coding: UTF-8 -*-
from packagesample import __version__, log


def main(xunxo, chicken):
    log.info("hello world submodule v" + __version__)
    log.debug("xunxo: " + xunxo)
    log.debug("chicken: " + str(chicken))
