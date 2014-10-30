# -*- coding: UTF-8 -*-
import glob
import os

__all__ = []

modules_folder = os.path.dirname(os.path.abspath(__file__))
py_files = glob.glob(modules_folder + '/*.py')
py_files.remove(os.path.abspath(__file__).replace('.pyc', '.py'))

for py_file in py_files:
    py_file = './' + '/'.join(py_file.split('/')[-3:])
    __all__.append(py_file.split('/')[3].split('.')[0])
