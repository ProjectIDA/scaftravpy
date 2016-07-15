#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a test module of the scaftravpy package.
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

    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File
           instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor
    """
    if not isinstance(n, (int, list)):
        raise TypeError(FIB_TYPE_ERROR)

    if isinstance(n, list):
        res = [fib(val) for val in n]
        return res
    else:
        if n < 0:
            raise ValueError(FIB_NEG_ERROR)

        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 1, 1
            for i in range(n-1):
                a, b = b, a+b
            return a
