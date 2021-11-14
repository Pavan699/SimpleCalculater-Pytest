#importing pytest
import pytest

# functions for calculater
def add(a,b):
    try:
        c=a+b
        return c
    except Exception as e:
        print("Exception is : ",e)

def sub(a,b):
    try:
        c=a-b
        return c
    except Exception as e:
        print("Exception is : ",e)

def multi(a,b):
    try:
        c=a*b
        return c
    except Exception as e:
        print("Exception is : ",e)

def div(a,b):
    try:
        c=a/b
        return c
    except Exception as e:
        print("Exception is : ",e)

#Tests for teh functions
def test_add():
    result = add(3,7)
    assert result == 10

def test_sub():
    result = sub(8,7)
    assert result == 1

def test_multi():
    result = multi(3,7)
    assert result == 21

def test_div():
    result = round(div(7,3))
    assert result == 2