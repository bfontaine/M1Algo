# -*- coding: UTF-8 -*-
from .base import algo

INF = float("inf")
PENALITY_SHORT = 1
PENALITY_LONG = 100

def test_wrap(words, count, cols, breaks, best, best_score, line_no, start, score):
    line = 0
    current_score = -1
    while( start <  count):
        # on remplie ligne, on test word[start]
        if line > 0:
            line = line + len(words[start])+1
        else :
            line = line + len(words[start])
        start+=1
        d = cols - line
        # on verifie quela taille de la ligne
        # courante est inférieure à la taille 
        # de la page 
        # on donne un score en conquence 
        if ((start < count) or (d < 0)):
            if ( d > 0):
                current_score = score + d * d * PENALITY_SHORT
            else :
                current_score = score + d * d * PENALITY_LONG
        else:
            current_score = score
        # si le score est supèrieur au best on revient en arriére
        if current_score >= best_score:
            if d <= 0 : return (1,best_score)
            continue
        best[line_no] = start
        (test,score_t) = test_wrap(words, count, cols, breaks, best, best_score, line_no+1, start, current_score)
        if test :
            best_score = score_t
    # on renvoie
    if (current_score >= 0) and (current_score < best_score):
        best_score = current_score
        for i in range(0,line_no+1):
            breaks[i] = best[i]
        return (1,best_score)
    return (0,best_score)

def balanced_wrap(words, count, cols, breaks):
    best = [0] * (count+1)
    # do a greedy wrap to have some baseline score to work with,
    # else we'll end up with O(2^N) behavior 
    best_score , breaks = greedy_wrap(words, count, cols, breaks)
    (test,score_t)= test_wrap(words, count, cols, breaks, best, best_score,0,0,0)
    if test :
        best_score = score_t

    return (best_score, breaks)


def show_wrap(words, len_w, breaks):
    lines = []
    count = 0
    for i in range(0,len_w):
        if breaks[i] == 0 : break
        line = []
        for j in range (count, breaks[i]):
            line.append(words[j])
        count = breaks[i]
        lines = lines + [line]
    return lines


@algo("use a balanced wrap algorithme")
def backtraking(words,width):
    words = list(words)
    len_words = len(words)
    if (len_words == 0):
        return [[]]
    l = [0] * (len_words + 1)
    (score,breaks) = balanced_wrap(words,len_words,width,l)
    return show_wrap(words,len_words,breaks)
