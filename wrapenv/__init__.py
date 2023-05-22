#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:     A module to wrap functions in an environment with pre- and post-processing functions.
# Project:     WrapEnv
#
# Author:      Anton G. Mueckl (amueckl@chartup.de)
#
# Created:     22.05.2023
# Copyright:   (c) Anton G. Mueckl (amueckl@chartup.de) 2023
# Licence:     MIT
# -------------------------------------------------------------------------------

from .wrapenv import environment
__all__ = (environment)
