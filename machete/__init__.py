# -*- coding: UTF-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301
import os
import sys
import logging
import getpass

__version__ = '0.0.1'
__author__ = 'Marco Lovato'
__author_username__ = 'lovato'
__author_email__ = 'maglovato@gmail.com'
__description__ = 'A simple python boilerplate - and multi template! - to start your python work.'
log = logging
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                filename='/tmp/machete-' + getpass.getuser() + '.log',
                filemode='a')


def __path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

if os.path.exists(__path('build.info')):
    __build__ = open(__path('build.info')).read().strip()
else:
    __build__ = '0'

__version__ = __version__ + '.' + __build__
