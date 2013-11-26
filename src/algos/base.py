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

def linelen(words):
    """
    Compute the length of a list of words as if they were put together on a
    line, with spaces between them.
    """
    words = [w for w in words]
    wcount = len(words)
    if wcount == 0:
        return 0
    return sum(map(len, words)) + wcount - 1

def simple_line_justifying(line, width):
    """
    Justify a line. 'line' is the list of words for this line, and 'width' the
    maximum output width.
    """
    wcount = len(line)
    if wcount < 2:
        return line

    length = linelen(line)
    if length >= width:
        return line

    lastword = line.pop()
    trailing = width - length
    spaces, onemore = divmod(trailing, wcount-1)
    sp  = ' ' * spaces
    sp2 = sp+' '
    line = list(map(lambda wi: wi[1]+(sp2 if wi[0] < onemore else sp), \
            enumerate(line)))
    line.append(lastword)
    return line

def justify(lines, width):
    """
    Justify a list of lines
    """
    for line in lines:
        yield simple_line_justifying(line, width)
