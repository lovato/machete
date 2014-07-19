#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Run the server in development mode.

from packagesample.start import app
app.run(host='0.0.0.0', debug=True)
