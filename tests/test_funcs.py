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


def test_fib1():
    ans = scaftravpy.funcs.fib(1)
    assert ans == 1


def test_fib_neg():
    with pytest.raises(ValueError) as e:
        scaftravpy.funcs.fib(-7)

    exception_raised = e.value
    assert str(exception_raised) == scaftravpy.funcs.FIB_NEG_ERROR


def test_fib_float():
    with pytest.raises(TypeError) as py_e:
        scaftravpy.funcs.fib(1.2)
    e = py_e.value
    assert str(e) == scaftravpy.funcs.FIB_TYPE_ERROR


def test_fib_good_list():
    inlst = [1, 2, 5, 7]
    outlst = scaftravpy.funcs.fib(inlst)
    assert outlst == [1, 1, 5, 13]


def test_fib_neg_list():
    inlst = [5, -5, 0, 1]
    with pytest.raises(ValueError) as py_e:
        scaftravpy.funcs.fib(inlst)
    e = py_e.value
    assert str(e) == scaftravpy.funcs.FIB_NEG_ERROR


def test_fib_float_list():
    inlst = [5, 0, 1.5, 9]
    with pytest.raises(TypeError) as py_e:
        scaftravpy.funcs.fib(inlst)
    e = py_e.value
    assert str(e) == scaftravpy.funcs.FIB_TYPE_ERROR