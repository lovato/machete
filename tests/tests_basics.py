# -*- coding: utf-8 -*-
# pylint: disable-msg=E0611

""" Example test to check version number """

from nose.tools import assert_equals  # @UnresolvedImport
from machete import __version__


def test_version():
    """ Base test to version method """

    assert_equals(type(__version__), str)
