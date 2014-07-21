# -*- coding: utf-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301

from machete import __version__, log
from machete.submodule import module
import argparse
import os

def main():
    log.info("machete v" + __version__)
    parser = argparse.ArgumentParser(description='machete v' + __version__)

    path = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "templates"))
    templates = [fn for fn in os.listdir(path) if any([not fn.startswith('_')])];

    for each in templates:
        print each

    parser.add_argument(
        '-t', '--template',
        help='Select one of the available templates. Allowed values are '+', '.join(templates),
        metavar='<template_name>',
        choices=templates, 
        required=True)
    parser.add_argument(
        "--chicken", help="Chicken mode (optional). Does NOT CHANGE anything.",
        action="store_true")
    args = parser.parse_args()

    try:
        module.main(args.template, args.chicken)
        exit(0)
    except Exception as e:
        import traceback
        log.error(traceback.format_exc())
        exit(1)
