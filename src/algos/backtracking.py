# -*- coding: UTF-8 -*-
from .base import algo

def greedy_wrap(words, count, cols, breaks):
    i = 0
    j = 0
    line = 0
    score = 0
    lens = list(map(len, words))
    while True:
        if i == count:
            breaks[j] = i
            j += 1
            break
        if line == 0:
            line += lens[i]
            i += 1
            continue
        if (line + lens[i] + 1 ) < cols:
            line += lens[i] + 1
            i += 1
            continue
        breaks[j] = i
        j += 1
        if i < count:
            d = cols - line
            p = d * d
            if d <= 0: p *= 100 # penalty
            score += p
        line = 0
    breaks[j] = 0
    return (score, breaks)

def balanced_wrap(words, breaks, count, width, best_score):
    lens = list(map(len, words))

    def bk(breaks, best, count, width, best_score, line_no=0, start=0, score=0):
        line = 0
        current_score = -1
        while start < count: # for each word
            # fill the line with the word's length
            if line > 0: line += 1
            line += lens[start]
            start += 1
            trailing = width - line
            p = 0 # penalty
            if start < count or trailing < 0:
                p = trailing * trailing
                if trailing <= 0: p *= 100

            current_score = score + p
            if current_score >= best_score:
                if trailing <= 0:
                    return best_score
                continue

            # if the current score is lower than the best score, we check all
            # possible arrangements on the next line
            best[line_no] = start
            best_score = bk(breaks, best, count, width, best_score, line_no + 1, start, current_score)
        # une fois qu'on à parcouru tout le tableau on test si le score courant est meilleur 
        # que le best_score , si oui on remplace les ligne 0 à notre line (line_no) dans breaks
        if 0 <= current_score < best_score:
            breaks[:line_no + 1] = best[:line_no + 1]
            return current_score

        return best_score

    best = [0] * (count + 1)
    bk(breaks, best, count, width, best_score)

@algo("A backtracking algorithm")
def backtracking(words, width):
    """
    <TODO>
    """
    words = list(words)
    count = len(words)
    if count == 0:
        yield []
        return
    breaks = [0] * (count + 1)

    # get an initial "best" score by applying 'greedy' on the words list
    best_score, breaks = greedy_wrap(words, count, width, breaks)

    balanced_wrap(words, breaks, count, width, best_score)

    start = 0
    for i in range(0, count):
        if breaks[i] == 0: break
        yield [words[j] for j in range(start, breaks[i])]
        start = breaks[i]

