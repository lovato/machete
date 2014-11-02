machete
=======

.. image:: https://travis-ci.org/lovato/machete.png?branch=master
    :target: https://travis-ci.org/lovato/machete

.. image:: https://coveralls.io/repos/lovato/machete/badge.png?branch=master 
   :target: https://coveralls.io/r/lovato/machete?branch=master

A command-line tool to create projects from templates, to start your python work.

To install it
-------------

::

    $ sudo pip install machete

Usage
-----

First, create your target directory, and cd to it.

Note: This directory must be empty. If you need to re-run machete, please empty the current folder first.

::

    usage: machete [-h] -t <template_name> [--chicken]

    machete vX

    optional arguments:
      -h, --help            show this help message and exit
      -t <template_name>, --template <template_name>
                            Select one of the available templates. Allowed values
                            are: app, bootstrap or flask.
      --chicken             Chicken mode (optional). Does NOT CHANGE anything.


Contributions
-------------

Bug reports, fixes, or features? Feel free to open an issue or pull request any time.

License
--------

Copyright (c) 2014 Marco Lovato Licensed under MIT_.

.. _MIT: http://opensource.org/licenses/MIT
