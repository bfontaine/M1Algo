# -*- coding: UTF-8 -*-
from .base import algo

PENALITY_SHORT = 1
PENALITY_LONG = 100

def greedy_wrap(words,count,cols,breaks):
    i = j = line = score = 0
    while(1):
        if i == count :
            breaks[j] = i
            j+=1
            break
        if line == 0 :
            line = len(words[i])
            i+=1
            continue
        if (line + len(words[i])) < cols:
            line += len(words[i])+1
            i+=1
            continue
        breaks[j] = i
        j+=1
        if (i < count):
            d = cols - line
            if ( d > 0): score += d * d * PENALITY_SHORT
            elif ( d < 0): score += d * d * PENALITY_LONG
        line = 0
    breaks[j] = 0
    return (score,breaks)

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


@algo("use a greedy wrap algorithme")
def word_wrap(words,width):
    words = list(words)
    len_words = len(words)
    if (len_words == 0):
        return [[]]
    l = [0] * (len_words + 1)
    (score,breaks) = greedy_wrap(words,len_words,width,l)
    return show_wrap(words,len_words,breaks)

@algo("use a balanced wrap algorithme")
def word_wrap_b(words,width):
    words = list(words)
    len_words = len(words)
    if (len_words == 0):
        return [[]]
    l = [0] * (len_words + 1)
    (score,breaks) = balanced_wrap(words,len_words,width,l)
    return show_wrap(words,len_words,breaks)
