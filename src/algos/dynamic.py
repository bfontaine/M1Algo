# -*- coding: UTF-8 -*-
from .base import algo

INF = float("inf")

def show_lines_wrap(words, lines, count): # TODO rename
    if lines[count] == 1:
        line = []
        for i in range(lines[count], count+1):
            line.append(words[i-1])
        return [line]

    p = show_lines_wrap(words, lines, lines[count]-1)
    p.append([words[i-1] for i in range(lines[count], count+1)])
    return p

def knuth_helper(words_len, count, width, exp=2):
    exp = max(1, exp)
    # lc[i][j] will have cost of a line which has words from i to j
    lc = [[0]*(count+1) for _ in range(count+1)]
    # tc[i] will have total cost of optimal arrangement of words 
    # from 1 to i
    tc = [0]*(count+1)
    # line is used to return the solution
    line = [0]*(count+1)
    # calculate extra space in a single line and line cost
    for i in range(1, count+1):
        # calculate extra spaces in a single line.
        # The value lc[i][j] indicates extra spaces 
        #    if words from word number i to j are
        #    placed in a single line
        lc[i][i] = width - words_len[i-1]
        for j in range(i+1, count+1):
            lc[i][j] = lc[i][j-1] - words_len[j-1] - 1
        # Calculate line cost corresponding to the above calculated extra spaces.
        # The value lc[i][j] indicates cost of putting words 
        #    from word number i to j in a single line
        for j in range(i, count+1):
            if lc[i][j] < 0:
                lc[i][j] = INF
            else:
                lc[i][j] = pow(lc[i][j], exp)

    # Calculate minimum cost and find minimum cost arrangement.
    # The value tc[j] indicates optimized cost to arrange words
    #    from word number 1 to j.
    for j in range(1, count+1):
        tc[j] = INF
        for i in range(1, j+1):
            if tc[i-1] != INF and lc[i][j] != INF and tc[i-1] + lc[i][j] < tc[j]:
                tc[j] = tc[i-1] + lc[i][j]
                line[j] = i
    return line

def knuth(words, width, exp):
    words = list(words)
    count = len(words)
    if (count == 0):
        return [[]]
    words_len = list(map(len, words))
    lines = knuth_helper(words_len, count, width, exp)
    para = show_lines_wrap(words, lines, count)
    return para

@algo("A Knuth-like dynamic programming algorithm using the square function")
def dynamic_2(words, width):
    return knuth(words, width, 2)

@algo("A Knuth-like dynamic programming algorithm using the cube function")
def dynamic_3(words, width):
    return knuth(words, width, 3)
