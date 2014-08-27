# -*- coding: UTF-8 -*-
import glob

__all__ = []

py_files = glob.glob('./packagesample/modules/*.py')
py_files.remove('./packagesample/modules/__init__.py')
for py_file in py_files:
	__all__.append(py_file.split('/')[3].split('.')[0])
