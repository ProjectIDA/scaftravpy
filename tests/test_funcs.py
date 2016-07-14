#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import scaftravpy.funcs

__author__ = "Dan Auerbach"
__copyright__ = "Dan Auerbach"
__license__ = "gpl3"


def test_fib_pos_int():
    assert scaftravpy.funcs.fib(7) == 13


def test_fib0():
    ans = scaftravpy.funcs.fib(0)
    assert ans == 0


def test_fib_neg():
    with pytest.raises(ValueError) as e:
        scaftravpy.funcs.fib(-7)

    exception_raised = e.value
    print(exception_raised)
    assert str(exception_raised) == scaftravpy.funcs.FIB_NEG_ERROR


def test_fib_float():
    with pytest.raises(TypeError):
        scaftravpy.funcs.fib(1.2)