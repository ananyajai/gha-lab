#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:18:59 2023

@author: ananya
"""

from myreverse import myreverse, isbn_checker
from hypothesis import given, strategies as st
import pytest
import unittest

@given(st.lists(st.integers()))
def test_myreverse(xs):
    assert xs == myreverse(myreverse(xs))
    

def test_isbn_checker():
    """ 
    Check that the a given string is a valid ISBN or not
    """
    assert isbn_checker("4370640407") == True, "This is a valid ISBN number"
    assert isbn_checker("689999139X") == True, "This is a valid ISBN number"
    assert isbn_checker("5370640407") == False, "This is not a valid ISBN number"


def test_empty_string():
    assert isbn_checker(" ") == False, "This is not a valid ISBN number"


@given(st.from_regex(r'[X][0-9]{9}'))
def test_isbn_invalid(x):
    assert isbn_checker(x) == False
    
    
    