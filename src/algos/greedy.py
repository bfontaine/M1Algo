# -*- coding: UTF-8 -*-
from .base import algo

@algo("The most basic greedy algorithm")
def naive_greedy(words, width):
    """
    This algorithm is the most basic one. It adds words to a line until it
    reaches the end of it, then continues on the next line.
    Its time complexity is linear and its memory one is constant, assuming
    the storage of the text is ignored.
    """
    line   = []
    # each word uses its length plus one space. To avoid exceptions, we assume
    # that the maximum width is larger by 1 space to include the last word's
    # one
    width += 1
    w = width
    for word in words:
        if len(word)+1 <= w or w == width:
            line.append(word)
            w -= len(word)+1
        else:
            yield line
            line = [word]
            w = width-len(word)-1

