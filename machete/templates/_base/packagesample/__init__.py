# -*- coding: UTF-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301
import os
import logging
import getpass
import tempfile

__version__ = '{{ packagesample.version }}'
__author__ = 'Your Name'
__author_username__ = 'your_username'
__author_email__ = 'yourname@gmail.com'
__description__ = 'Generated from a template'


log_filename = os.path.join(tempfile.gettempdir(),
                            'packagesample-' + getpass.getuser() + '.log')
log_format = '%(asctime)s %(levelname)-5s %(filename)+12s:%(lineno)03d %(message)s (%(name)s)'

logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    filename=log_filename,
                    filemode='a')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter(log_format)
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

log = logging.getLogger('packagesample')

def __path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

# Jenkins
if os.getenv("BUILD_NUMBER"):
    file_ = open(__path('build.info'), 'w')
    file_.write(os.getenv("TRAVIS_BUILD_NUMBER"))
    file_.close()

# Travis
if os.getenv("TRAVIS_BUILD_NUMBER"):
    file_ = open(__path('build.info'), 'w')
    file_.write(os.getenv("TRAVIS_BUILD_NUMBER"))
    file_.close()

__build__ = '0'
if os.path.exists(__path('build.info')):
    __build__ = open(__path('build.info')).read().strip()

__version__ = __version__ + '.' + __build__
