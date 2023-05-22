import sys
import os
import importlib

# PATH_TO_PYTHON_INSTALLATION = r'C:\Program Files (x86)\Python38'
PATH_TO_PYTHON_INSTALLATION = r'C:\Program Files\Python311'
PYTHONPATH = os.environ.get('PYTHONPATH', PATH_TO_PYTHON_INSTALLATION)
LIB_FOLDERS = ['DLLs', 'Lib', '', 'Lib\\site-packages']
for folder in LIB_FOLDERS:
    sys.path.append(os.path.join(PYTHONPATH, folder))
    pass

import xmlrpc.client                    # see Discussion https://github.com/orgs/pyinstaller/discussions/7645
print(dir(xmlrpc.client)[0:3])

plugin = importlib.import_module('plugin')
print(dir(plugin.xmlrpc.server)[0:3])
