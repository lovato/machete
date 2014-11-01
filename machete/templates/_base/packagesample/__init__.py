# -*- coding: UTF-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301
import os
import logging
import getpass
import tempfile

__version__ = '0.0.1'
__author__ = 'Your Name'
__author_username__ = 'your_username'
__author_email__ = 'yourname@gmail.com'
__description__ = 'Generated from a template'
__chicken__ = False

log_filename = os.path.join(tempfile.gettempdir(),
                            'packagesample-' + getpass.getuser() + '.log')

log = logging
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                filename=log_filename,
                filemode='a')


def __path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

if os.path.exists(__path('build.info')):
    __build__ = open(__path('build.info')).read().strip()
else:
    __build__ = '0'

__version__ = __version__ + '.' + __build__
