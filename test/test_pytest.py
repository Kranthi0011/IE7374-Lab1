import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(3, 2) == 5
    assert fun1(-1, 1) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(0, 5) == -5

def test_fun3():
    assert fun3(4, 3) == 12
    assert fun3(-2, 3) == -6

def test_fun4():
    assert fun4(3, 2) == 12
