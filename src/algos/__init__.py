# -*- coding: UTF-8 -*-
import os
import importlib
from glob import glob
from .base import get_algos, justify

# Import all files from this directory as modules
files = glob(os.path.dirname(__file__)+"/*.py")
modules = [ os.path.basename(f)[:-3] for f in files ]
for m in modules:
    if m.startswith('__') or m == 'base':
        continue
    importlib.import_module('.'+m, 'algos')
