#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        test_example2.py
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


def test_example2():
    # Create an instance of the ENVIRONMENT class
    env = environment

    # Define a function that multiplies a number by 2
    def multiply_by_two(x):
        return x * 2

    # Define a preprocessing function that adds 1 to the argument
    def preprocessing_fn(env, fn):
        fn.args[0] += 1

    # Define a postprocessing function that subtracts 5 from the result
    def postprocessing_fn(env, fn):
        fn.result -= 5

    # Register the function and preprocessing/postprocessing functions in the environment
    env.register_function(multiply_by_two)
    env.register_preprocessing(multiply_by_two, preprocessing_fn)
    env.register_postprocessing(multiply_by_two, postprocessing_fn)

    # Execute the function with an argument
    result = env.run_API_cmd(multiply_by_two, 10)       # 10 + 1 = 11, 11 * 2 = 22, 22 - 5 = 17

    # Check the result
    assert result == 17, "Incorrect result"

    # clear the *args list, since there will be a new function call providing a new *args list
    env.clear_arguments(multiply_by_two)


    # Alternatively, you can use the following syntax:
    result = env.multiply_by_two(15)                    # 15 + 1 = 16, 16 * 2 = 32, 32 - 5 = 27
    assert result == 27, "Incorrect result"

    print("Example 2 test passed!")


# Run the test function
if __name__ == '__main__':
    test_example2()
