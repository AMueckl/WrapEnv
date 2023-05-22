#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        test_example1.py
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

from wrapenv import environment

def test_example1():
    # Create an instance of the ENVIRONMENT class
    env = environment

    # Define a simple function
    def add_numbers(a, b):
        return a + b

    # Register the function in the environment
    env.register_function(add_numbers)

    # Execute the function with arguments
    result = env.run_API_cmd(add_numbers, 2, 3)

    # Check the result
    assert result == 5, "Incorrect result"

    print("Example 1 test passed!")

# Run the test function
if __name__ == '__main__':
    test_example1()
