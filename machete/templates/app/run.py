#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Run the app

from ipdb import launch_ipdb_on_exception
from packagesample import start

with launch_ipdb_on_exception():
    start.main()
