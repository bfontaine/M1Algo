# -*- coding: UTF-8 -*-
from .base import algo, linelen

def naive_dc_helper(words, width, llen):
    if llen <= width:
        return [words]

    middle = len(words) // 2
    part1, part2 = words[:middle], words[middle:]
    len1 = linelen(part1)
    len2 = llen - len1 - 1
    return naive_dc_helper(part1, width, len1) \
         + naive_dc_helper(part2, width, len2)


@algo("A basic divide & conquer algorithm")
def naive_dc(words, width):
    """
    This algorithm divides the text recursively in parts until each part
    can be included on its own line. Thus, it can only work on a finite list
    of words.
    """
    words = list(words)
    for line in naive_dc_helper(words, width, linelen(words)):
        yield line


def alternate_dc_helper(words, width):
    length_words = len(words)
    line = []
    if length_words == 0: return ([], words, 0)
    if length_words == 1: return ([], words, len(words[0]))

    middle = length_words // 2
    if length_words % 2 == 1: middle += 1

    lines1, line1, len1 = alternate_dc_helper(words[:middle], width)
    lines2, line2, len2 = alternate_dc_helper(words[middle:], width)

    if lines2 == []:
        total = len1 + len2 + 1
        if total <= width:
            return (lines1, line1 + line2, total)

        # not sure that the two lines below are necessary
        lines1.append(line1)
        return (lines1, line2, len2)

    lines1.append(line1)
    return (lines1 + lines2, line2, len2)


@algo("Another divide & conquer algorithm")
def alternative_dc(words, width):
    """
    This algorithm recursively splits the list into two parts until having only
    one word in each one. It then reduces the number of parts by concatenating
    them until each one reaches the maximum line width.
    """
    lines, lastline, _ = alternate_dc_helper(list(words), width)
    lines.append(lastline)
    return lines
