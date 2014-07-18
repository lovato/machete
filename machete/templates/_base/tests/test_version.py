# -*- coding: utf-8 -*-
# pylint: disable-msg=E0611

""" Example test to check version number """

from nose.tools import assert_equals  # @UnresolvedImport
from packagesample import __version__


def test_version():
    """ Base test to version method """

    base_version = '0.0.1.0'

    assert_equals(base_version, __version__)
