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

def justify_line(line, width): # TODO test me
    """
    Justify a line. 'line' is the list of words for this line, and 'width' the
    maximum output width.
    """
    wcount = len(line)
    length = wcount + sum(map(len, line)) - 1
    if wcount < 2 or length >= width:
        return line

    lastword = line.pop()
    trailing = width-length-1
    spaces, onemore = divmod(trailing, wcount)
    sp  = ' '*spaces
    sp2 = sp+' '
    line.append(lastword)
    line[:-1] = map(lambda wi: wi[1]+(sp2 if wi[0] < onemore else sp), \
            enumerate(line[:-1]))
    return line

def justify(func):
    """
    A decorator for algorithms functions to yield justified lines. This
    slightly increase the run time but avoid a lot of code duplication. It
    adds O(n) to the overall complexity of the algorithm, but since we can't
    have lower complexities it's not _that_ annoying.
    """
    def wrapper(txt, width):
        for line_words in func(txt, width):
            yield justify_line(line_words, width)

    name = func.__name__
    wrapper.__name__ = name + '_justify'
    name = name.replace('_', '-')
    wrapper.__doc__  = '\n    See \'%s\'.\n' % name
    register(wrapper, 'Same as %s with justifying' % name)
    return func

def linelen(words):
    """
    Compute the length of a list of words as if they were put together on a
    line, with spaces between them.
    """
    words = [w for w in words]
    wcount = len(words)
    return sum(map(len, words)) + wcount -1
