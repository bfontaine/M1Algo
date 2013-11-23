# -*- coding: UTF-8 -*-
import itertools
from .base import algo

@algo("The most basic greedy algorithm")
def simple_greedy(words, width):
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

    yield line

@algo("Balanced variant of simple-greedy")
def balanced_greedy(words, width):
    """
    This algorithm calls simple-greedy, compute the average inter-word break
    length, set every inter-word length to this average, and re-run the simple
    greedy algorithm on this. It thus runs in O(3n) (memory: O(n)).
    """
    avglen = 0 # average
    bkcount = 0 # count of breaks

    lines = [x for x in simple_greedy(words, width)]

    for line in lines:
        lbkcount = len(line) - 1
        trailing = width - sum(map(len, line)) - lbkcount
        bkcount += lbkcount
        avglen += trailing

    avglen //= max(bkcount, 1)
    spaces = ' '*avglen

    for i, line in enumerate(lines):
        lines[i][:-1] = map(lambda w:w+spaces, line[:-1])

    return simple_greedy(itertools.chain(*lines), width)
