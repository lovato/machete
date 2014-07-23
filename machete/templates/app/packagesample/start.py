# -*- coding: utf-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301

from packagesample import __version__, log
from packagesample.submodule import module
import argparse


def main():
    log.info("packagesample v" + __version__)
    parser = argparse.ArgumentParser(
        description='packagesample v' + __version__)

    parser.add_argument(
        '-x', '--xunxo', help='Sample Required Parameter', required=True)
    parser.add_argument(
        "--chicken",
        help="Chicken mode (optional). Does NOT CHANGE anything.",
        action="store_true")
    args = parser.parse_args()  # if required params arent met, program aborts
    try:
        module.main(args.xunxo, args.chicken)
        exit(0)
    except Exception as e:
        import traceback
        log.error(traceback.format_exc())
        exit(1)
