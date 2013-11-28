# -*- coding: UTF-8 -*-
from .base import algo

INF = float("inf")

def knuth(words_len, count, width, exp=2):
    # lc[i][j] stores the cost of a line which has the i-th to the j-th words
    lc = [[0]*(count+1) for _ in range(count+1)]

    # We can't fit more than width/2 words on a line, because they are
    # separated by at least one space, e.g.:
    # width=3 -> 'a b' (max. 2 words)
    # width=8 -> 'a b c d ' (max. 4 words)
    d, m = divmod(width, 2)
    maxwords = d + m # width/2 + width %2

    # compute the cost for each possible line by weighting them according to
    # trailing spaces at their end. A line that can't fit as an infinite cost,
    # a line that perfectly fit has a cost of zero, and other ones have their
    # cost set to either the square or the cube of the number of trailing
    # spaces. The choice of square or cube is made using the 'exp' argument
    # (e.g. 2 -> square, 3 -> cube).
    lc_tmp = 0
    for i in range(1, count+1):
        # lc[i][j] stores the number of trailing spaces if words from i to j
        # were put in one line
        for j in range(i, count+1):
            if j == i :
                lc[i][i] = width - words_len[i-1]
            else :
                lc[i][j] = lc_tmp - words_len[j-1] - 1
            lc_tmp = lc[i][j]
        # We then compute the cost according to the number of trailing spaces.
        # Thus, lc[i][j] is the cost of putting words i to j on a single line.
            if lc[i][j] < 0:
                lc[i][j] = INF
            elif j == count:
                lc[i][j] = 0 # The last line has no cost if it can fit
            else:
                lc[i][j] = pow(lc[i][j], exp)

    # tc[i] will have total cost of optimal arrangement of words
    # from 1 to i
    tc = [0]*(count+1)
    # line is used to return the solution
    line = [0]*(count+1)

    # Calculate minimum cost and find minimum cost arrangement.
    # The value tc[j] indicates optimized cost to arrange words
    #    from word number 1 to j.
    for j in range(1, count+1):
        tc[j] = INF
        for i in range(1, j+1):
            if tc[i-1] != INF and lc[i][j] != INF \
                        and tc[i-1] + lc[i][j] < tc[j]:
                tc[j] = tc[i-1] + lc[i][j]
                line[j] = i
    return line

def dynamic_helper(words, width, exp):
    # This function is here only to remove duplicate code from dynamic_{2,3}
    words = list(words)
    count = len(words)
    if (count == 0):
        return [[]]
    words_len = list(map(len, words))
    lines = knuth(words_len, count, width, exp)
    p = []
    while lines[count] >= 1:
        p.append([words[i-1] for i in range(lines[count], count+1)])
        count = lines[count] - 1

    p.reverse()
    return p

@algo("A Knuth-like dynamic programming algorithm using the square function")
def dynamic_2(words, width):
    return dynamic_helper(words, width, 2)

@algo("A Knuth-like dynamic programming algorithm using the cube function")
def dynamic_3(words, width):
    return dynamic_helper(words, width, 3)
