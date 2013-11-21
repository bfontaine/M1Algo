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

def simple_line_justifying(line, width):
    """
    Justify a line. 'line' is the list of words for this line, and 'width' the
    maximum output width.
    """
    wcount = len(line)
    if wcount < 2:
        return line

    length = sum(map(len, line)) + wcount - 1
    if length >= width:
        return line

    lastword = line.pop()
    trailing = width-length
    spaces, onemore = divmod(trailing, wcount-1)
    sp  = ' '*spaces
    sp2 = sp+' '
    line.append(lastword)
    line[:-1] = map(lambda wi: wi[1]+(sp2 if wi[0] < onemore else sp), \
            enumerate(line[:-1]))
    return line

def dynamic_justifying(lines, width):
    """
    Justify a text by using a method inspired from Hana Samet's paper,
    "Heuristics for the Line Division Problem in Computer Justified Text"
    (published in 1981).
    """
    # TODO
    return lines

def justify(lines, width, **kwargs):
    """
    A decorator for algorithms functions to yield justified lines. This
    slightly increase the run time but avoid a lot of code duplication. It
    adds O(n) to the overall complexity of the algorithm, but since we can't
    have lower complexities it's not _that_ annoying.
    """
    kwargs.setdefault('method', 'simple')
    mth = kwargs['method']

    if mth == 'simple' or mth not in ['simple', 'dynamic']:
        for line in lines:
            yield simple_line_justifying(line, width)
        return

    # dynamic
    return dynamic_justifying(lines, width)

def linelen(words):
    """
    Compute the length of a list of words as if they were put together on a
    line, with spaces between them.
    """
    words = [w for w in words]
    wcount = len(words)
    return sum(map(len, words)) + wcount -1
