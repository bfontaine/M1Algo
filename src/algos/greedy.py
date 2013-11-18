# -*- coding: UTF-8 -*-
from .base import algo

def justify(line, length, width):
    """
    Justify a line. 'line' is the list of words for this line, 'length' is its
    total width with one space between each pair of words, and 'width' the
    maximum output width.
    """
    wcount = len(line)
    if wcount < 2 or length >= width:
        return ' '.join(line)

    lastword = line.pop()
    trailing = width-length-1
    spaces, onemore = divmod(trailing, wcount)
    sp  = ' '*spaces
    sp2 = sp+' '
    line = map(lambda wi: wi[1]+(sp2 if wi[0] < onemore else sp), \
            enumerate(line))
    return ' '.join(line) + ' ' + lastword


@algo("The most basic greedy algorithm")
def naive_greedy(words, width):
    """
    This algorithm is the most basic one. It adds words to a line until it
    reaches the end of it, then continues on the next line.
    Its time complexity is linear and its memory one is constant, assuming
    the storage of the text is ignored.
    """
    line = []
    # each word uses its length plus one space. To avoid exceptions, we assume
    # that the maximum width is larger by 1 space to include the last word's
    # one
    width += 1
    w = width
    for word in words:
        lw = len(word)
        if lw+1 <= w or w == width:
            line.append(word)
            w -= lw+1
        else:
            yield ' '.join(line)
            line = [word]
            w = width-lw-1


@algo("Naive greedy with justifying")
def naive_greedy_justify(words, width):
    """
    See naive-greedy for the details.
    """
    line = []
    linelen = 0
    width += 1
    w = width
    for word in words:
        lw = len(word)
        if lw+1 <= w or w == width:
            line.append(word)
            linelen += lw + 1
            w -= lw + 1
        else:
            yield justify(line, linelen-1, width)
            line = [word]
            linelen = lw + 1
            w = width - linelen

