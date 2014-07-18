# -*- coding: utf-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301

from machete import __version__, log
from machete.submodule import module
import argparse


def main():
    log.info("machete v" + __version__)
    parser = argparse.ArgumentParser(description='machete')

    parser.add_argument(
        '-t', '--template',
        help='Select one of the available templates (TODO list them here).',
        required=True)
    parser.add_argument(
        '-p', '--project',
        help='Please specify how your project will be named.',
        required=True)
    parser.add_argument(
        "--chicken", help="Chicken mode (optional). Does NOT CHANGE anything.",
        action="store_true")
    args = parser.parse_args()
    # if required params are not met, program aborts here
    try:
        module.main(args.template,
                    args.project.replace('-', '_'), args.chicken)
        exit(0)
    except Exception as e:
        import traceback
        log.error(traceback.format_exc())
        exit(1)
