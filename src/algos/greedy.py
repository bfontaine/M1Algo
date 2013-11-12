# -*- coding: UTF-8 -*-
import re
from .base import algo

@algo("The most basic greedy algorithm")
def naive_greedy(txt, width):
    """
    This algorithm is the most basic one. It adds words to a line until it
    reaches the end of it, then continues on the next line.
    Its time complexity is linear and its memory one is constant, assuming
    the storage of the text is ignored.
    """
    lines = [[]]
    line = 0
    # each word uses its length plus one space. To avoid exceptions, we assume
    # that the maximum width is larger by 1 space to include the last word's
    # one
    width += 1
    w = width
    for x in re.finditer(r'\w+', txt):
        word = x.group(0)
        if len(word)+1 <= w or w == width:
            lines[line].append(word)
            w -= len(word)+1
        else:
            line += 1
            lines.append([word])
            w = width-len(word)-1

    return lines
