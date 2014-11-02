# -*- coding: UTF-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301
import os
import sys
import logging
import getpass
import tempfile

__version__ = '0.0.2'
__author__ = 'Marco Lovato'
__author_username__ = 'lovato'
__author_email__ = 'maglovato@gmail.com'
__description__ = 'A command-line tool to create projects \
                  from templates, to start your python work.'

log_filename = os.path.join(tempfile.gettempdir(),
                            'machete-' + getpass.getuser() + '.log')

log = logging
log.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s',
                filename=log_filename,
                filemode='a')


def __path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

if os.getenv("TRAVIS_BUILD_NUMBER"):
    file_ = open(__path('build.info'), 'w')
    file_.write(os.getenv("TRAVIS_BUILD_NUMBER"))
    file_.close()

if os.path.exists(__path('build.info')):
    __build__ = open(__path('build.info')).read().strip()
else:
    __build__ = '0'

__version__ = __version__ + '.' + __build__
