#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        test_examples.py
# Purpose:
# Project:     WrapEnv
#
# Author:      Anton G. Mueckl (amueckl@chartup.de)
#
# Created:     22.05.2023
# Copyright:   (c) Anton G. Mueckl (amueckl@chartup.de) 2023
# Licence:     Property of the author (see above).
#              Do not use without prior written permission.
# -------------------------------------------------------------------------------

import unittest
from test_example1 import test_example1
from test_example2 import test_example2
from test_example3 import test_example3


class ExampleTestSuite(unittest.TestSuite):
    def __init__(self):
        super().__init__()
        self.addTest(unittest.FunctionTestCase(test_example1))
        self.addTest(unittest.FunctionTestCase(test_example2))
        self.addTest(unittest.FunctionTestCase(test_example3))


def main():
    suite = ExampleTestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
