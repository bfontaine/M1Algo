#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from .base import algo

@algo("does nothing, just an example")
def nothing(txt, wd):
    """
    An example function
    """
    return [txt]

@algo()
def abc(txt, wd):
    """
    Another example
    """
    return ["a", "b", "c"]
