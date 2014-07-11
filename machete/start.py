# -*- coding: utf-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301

from machete import __version__, log
from machete.submodule import module
import argparse

def main():
    log.info("machete START v" + __version__)
    parser = argparse.ArgumentParser(description='Sample Project')

    parser.add_argument(
        '-x', '--xunxo', help='Sample Required Parameter', required=True)
    parser.add_argument(
        "--chicken", help="Chicken mode (optional). Only shows what to do. Does NOT CHANGE anything.", action="store_true")
    args = parser.parse_args() #if required params are not met, program aborts here
    try:
        module.main(args.xunxo, args.chicken)
        exit(0)
    except Exception as e:
        import traceback
        log.error(traceback.format_exc())
        exit(1)
