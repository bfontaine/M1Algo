#! /usr/bin/env python
# -*- coding: UTF-8 -*-

ALGOS = {}

def register(func, shortdoc):
    """
    Register an algorithm function
    """
    global ALGOS
    ALGOS[func.__name__] = [func, shortdoc]

def get_algos():
    """
    Return a dict of all registered algorithms
    """
    global ALGOS
    return ALGOS

def algo(doc=""):
    """
    A decorator for algorithms functions which add the decorated functions
    to a global register
    """
    def wrapper(func):
        register(func, doc)
        return func
    return wrapper
