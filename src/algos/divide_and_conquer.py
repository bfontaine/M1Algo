# -*- coding: UTF-8 -*-
from .base import algo, linelen

def naive_dc_helper(words, width, llen):
    if llen <= width:
        return [words]

    wcount = len(words)
    if wcount <= 1:
        return [words]

    middle = wcount // 2
    part1 = words[:middle]
    part2 = words[middle:]
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


def opt_dc_helper(words, width): # TODO explain how it works
    length_words = len(words)
    line = []
    if length_words == 0:
        return ([], (words, 0))
    if length_words == 1:
        return (line,(words,len(words[0])))
    length_words2 = length_words // 2
    words1 = words[:length_words2]
    words2 = words[length_words2:]
    lines1, (line1, l_length1) = opt_dc_helper(words1, width)
    lines2, (line2, l_length2) = opt_dc_helper(words2, width)
    # partie f(n)
    if lines2 == []:
        total = l_length1 + l_length2 + 1
        if total <= width:
            return (lines1, (line1 + line2, total))
        lines1.append(line1)
        return (lines1, (line2, l_length2))

    lines1.append(line1)
    lines1 = lines1 + lines2
    return (lines1, (line2, l_length2))


@algo("A optimized divide & conquer algorithm")
def opt_dc(words, width): # TODO fix the doc
    """
    This algorithm recursively splits the list into two, to have only one word.
    returns (list_line (current_line, length_line))
    """
    words = list(words)
    lines, (word, l_length) = opt_dc_helper(words, width)
    lines.append(word)
    return lines
