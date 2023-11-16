#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:17:41 2023

@author: ananya
"""
import sys

def myreverse(x): 
    return x[::-1]

def isbn_checker(x):
    if x == " ":
        return False
    isbn = list(x)
    if isbn[-1] == 'X' or isbn[-1] == 'x':
        isbn[-1] = 10
    if isbn.count('X') != 0:
        return False
    if sum([ int(isbn[i])*(i+1) for i in range(10) ])%11 == 0:
        return True
    else:
        return False
    
    


