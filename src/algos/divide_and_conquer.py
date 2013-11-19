# -*- coding: UTF-8 -*-
from .base import algo, justify, linelen

def naive_dc_helper(words, width, llen):
    wcount = len(words)
    if wcount <= 1:
        return [words]
    if llen <= width:
        return [words]

    middle = wcount//2
    part1 = words[:middle]
    len1 = linelen(part1)
    return naive_dc_helper(part1, width, len1) \
        + naive_dc_helper(words[middle:], width, llen-len1)

@justify
@algo("A basic divide & conquer algorithm")
def naive_dc(words, width):
    """
    This algorithm divides the text recursively in parts until each part
    can be included on its own line. Thus, it can only work on a finite list
    of words.
    """
    words = [w for w in words]
    for line in naive_dc_helper(words, width, linelen(words)):
        yield line

