#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        run_pyinstaller.py
# Purpose:
# Project:     code_pyside2
#
# Author:      Anton G. Mueckl (amueckl@chartup.de)
#
# Created:     19.05.2023
# Copyright:   (c) Anton G. Mueckl (amueckl@chartup.de) 2023
# Licence:     MIT
# -------------------------------------------------------------------------------

from PyInstaller import __main__ as pyi
from wrapenv import environment, ENVIRONMENT, Function

import sys, os, shutil, glob
import pkgutil

MAXLOOPS = 10


python_base = os.path.dirname(sys.base_prefix)

def analysis_preprocessor(environment:ENVIRONMENT, fn:Function):
    print('analysis_preprocessor for {}'.format(fn._name))

    fn._local_env['accessible_modules'] = pkgutil.walk_packages()
    ap = dict()
    count = 0
    for module in fn._local_env['accessible_modules']:
        if module.ispkg or True:
            module_name = module.name
            finder = module.module_finder
            path = finder.path
            if not path.startswith(python_base):
                continue
            if module_name.count('.') == 0:
                continue
            module_base = module_name.split('.')[0]
            if module_base not in ap.keys():
                ap[module_base] = list()
                pass
            ap[module_base].append(module_name)
            count += 1
            pass
        pass

    fn._local_env['accessible_packages'] = ap
    fn._local_env['accessible_packages_count'] = count
    fn._local_env['analyzed_modules_count'] = 0
    fn._local_env['loops'] = 0
    fn._local_env['maxloops'] = MAXLOOPS
    pass

def analysis_check(environment:ENVIRONMENT, fn:Function):
    print('analysis_check for {}'.format(fn._name))
    result = fn.result
    ap = dict()
    count = 0

    for package in result.pure:
        (name, path, info) = package
        if not path.startswith(python_base):
            continue
        if name.count('.') == 0:
            continue
        module_base = name.split('.')[0]
        if module_base not in ap.keys():
            ap[module_base] = list()
            pass
        ap[module_base].append(name)
        count += 1
        pass

    hiddenimports = fn.kwargs.get('hiddenimports', [])
    for module_base in ap.keys():
        if module_base not in hiddenimports:
            hiddenimports.append(module_base)
            pass
        for module in fn._local_env['accessible_packages'][module_base]:
            if module not in hiddenimports:
                hiddenimports.append(module)
                pass
            pass
        pass
    fn.kwargs['hiddenimports'] = hiddenimports

    fn._local_env['analyzed_modules'] = ap
    former_count = fn._local_env['analyzed_modules_count']
    fn._local_env['analyzed_modules_count'] = count
    return fn._local_env['analyzed_modules_count'] == former_count or fn._local_env['loops'] >= fn._local_env['maxloops']

def analysis_modify(environment:ENVIRONMENT, fn:Function):
    print('analysis_modify for {}'.format(fn._name))
    fn._local_env['loops'] += 1
    print(f"{fn._local_env['loops']=}")
    pass

def analysis_postprocessor(environment:ENVIRONMENT, fn:Function):
    print('analysis_postprocessor for {}'.format(fn._name))
    print(f"{fn._local_env['loops']=}")
    pass

def pre_compile(environment: ENVIRONMENT):
    environment.register_preprocessing('Analysis', analysis_preprocessor)
    environment.register_check('Analysis', analysis_check)
    environment.register_modify('Analysis', analysis_modify)
    environment.register_postprocessing('Analysis', analysis_postprocessor)
    pass

def run_compile(environment: ENVIRONMENT):
    pyi.run(["--noconfirm", "main_special.spec"])
    pass

def post_compile(environment: ENVIRONMENT):
    DISTPATH = environment['DISTPATH']

    # source: https://stackoverflow.com/questions/47850064/add-config-file-outside-pyinstaller-onefile-exe-into-dist-directory

    working_dir_files = [
            ('common', 'main/common'),
            ('configuration', 'main/configuration'),
            ('plugins', 'main/plugins'),
    ]

    def copy_folders_to(DISTPATH):
        print(os.getcwd())
        for tup in working_dir_files:
            print(tup)
            to_path = os.path.join(DISTPATH, tup[1])
            if os.path.exists(to_path):
                if os.path.isdir(to_path):
                    shutil.rmtree(to_path)
                else:
                    os.remove(to_path)
            print(f'copying {tup[0]} to {to_path}')
            if os.path.isdir(tup[0]):
                shutil.copytree(tup[0], to_path)
            else:
                shutil.copyfile(tup[0], to_path)

    copy_folders_to(DISTPATH)
    pass

def run_main(environment):
    pre_compile(environment)
    run_compile(environment)
    post_compile(environment)
    pass

if __name__ == '__main__':
    run_main(environment)
