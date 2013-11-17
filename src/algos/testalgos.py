#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from .base import algo

@algo("does nothing, just an example")
def nothing(words, wd):
    """
    An example function
    """
    yield [w for w in words]

@algo()
def abc(words, wd):
    """
    Another example
    """
    for l in ["a", "b", "c"]:
        yield l
