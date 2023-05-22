#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        test_example3.py
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

def test_example3():
    # Create an instance of the ENVIRONMENT class
    env = environment

    # Define a function that doubles a number
    def double_number(x):
        return x * 2

    # Define a check function that checks if the result is less than 100
    def check_fn(env, fn):
        return fn.result == 100

    # Define a modify function that increments the argument by 1
    def modify_fn(env, fn):
        fn.args[0] += 1

    # Register the function, check function, and modify function in the environment
    env.register_function(double_number)
    env.register_check(double_number, check_fn)
    env.register_modify(double_number, modify_fn)

    # Execute the function with an argument that starts at 1
    result = env.run_API_cmd(double_number, 1)                  # starting off with 1, incrementing by 1, doubling the result

    # Check the result
    assert result == 100, "Incorrect result"

    print("Example 3 test passed!")


# Run the test function
if __name__ == '__main__':
    test_example3()

