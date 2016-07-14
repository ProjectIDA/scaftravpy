#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     fibonacci = scaftravpy.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import logging

from scaftravpy import __version__

__author__ = "Dan Auerbach"
__copyright__ = "Dan Auerbach"
__license__ = "gpl3"

_logger = logging.getLogger(__name__)

FIB_NEG_ERROR = 'Can not calculate the fibonoci value of a negative number.'
FIB_TYPE_ERROR = 'Fib(n) only accepts an integer..'

def fib(n):
    """
    Fibonacci example function

    :param n: integer
    :return: n-th Fibonacci number
    """
    if not isinstance(n, int):
        raise TypeError(FIB_TYPE_ERROR)
    
    if n < 0:
        raise ValueError(FIB_NEG_ERROR)

    elif n == 0:
        return 0
    else:
        a, b = 1, 1
        for i in range(n-1):
            a, b = b, a+b
        return a
