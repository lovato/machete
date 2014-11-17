# -*- coding: utf-8 -*-
# pylint: disable-msg=E0611

""" Example test to check version number """

from nose.tools import assert_equals  # @UnresolvedImport
from machete.submodule import module


def test_os_call():
    feedback = module.os_call('echo 1')
    assert_equals(feedback, '1\n')
