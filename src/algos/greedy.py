# -*- coding: UTF-8 -*-
from .base import algo, justify

@justify
@algo("The most basic greedy algorithm")
def naive_greedy(words, width):
    """
    This algorithm is the most basic one. It adds words to a line until it
    reaches the end of it, then continues on the next line.
    Its time complexity is O(n) and its memory one is O(k), where n is the
    length of the text and k the maximum width.
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
            yield line
            line = [word]
            w = width-lw-1

