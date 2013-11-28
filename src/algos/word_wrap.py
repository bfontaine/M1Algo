# -*- coding: UTF-8 -*-
from .base import algo

PENALTY_SHORT = 1
PENALTY_LONG = 100

def greedy_wrap(words,count,cols,breaks):
    i = j = line = score = 0
    while(1):
        if i == count :
            breaks[j] = i
            j+=1
            break
        len_word = len(words[i])
        if line == 0:
            line += len_word
            i+=1
            continue;
        if (line + len_word +1 ) < cols:
            line += len_word + 1
            i+=1
            continue;
        breaks[j]=i
        j+=1
        if (i < count):
            d = cols - line
            if (d > 0):  score += PENALTY_SHORT * d * d
            else:        score += PENALTY_LONG * d * d
        line = 0;
    breaks[j] = 0
    return (score,breaks)

def balanced_wrap(words, breaks, best, count, cols, best_score, line_no, start, score):
    line = 0
    current_score = -1
    # on parcourt le tableau de mot un par un
    while( start <  count):
        # on remplie la ligne avec la taille du mot
        if line > 0:
            line = line + len(words[start])+1
        else :
            line = line + len(words[start])
        start+=1
        # d représente le nombre d'espace en fin de ligne
        d = cols - line
        # on donne un score à la ligne ,qu'n ajoute au score globale
        if ((start < count) or (d < 0)):
            if ( d > 0):
                current_score = score + d * d * PENALTY_SHORT
            else :
                current_score = score + d * d * PENALTY_LONG
        else:
            current_score = score
        # Si
        if current_score >= best_score:
            if d <= 0 : return (1,best_score)
            continue
        # si le score courant est inférieur aux meilleur score
        # on test les cas, en se placant à la ligne suivante
        best[line_no] = start
        (test,score_t) = balanced_wrap(args_tab, line_no+1, start, current_score)
        if test :
            best_score = score_t
    # une fois qu'on à parcouru tout le tableau on test si le score courant est meilleur 
    # que le best_score , si oui on remplace les ligne 0 à notre line (line_no) dans breaks
    if (current_score >= 0) and (current_score < best_score):
        best_score = current_score
        for i in range(0,line_no+1):
            breaks[i] = best[i]
        return (1,best_score)
    # si ce n'est pas meilleur on ne prend du score courant
    return (0,best_score)

def show_wrap(words, count, breaks):
    lines = []
    start = 0
    for i in range(0,count):
        if breaks[i] == 0 : break
        line = []
        for j in range (start, breaks[i]):
            line.append(words[j])
        start = breaks[i]
        lines.append(line)
    return lines


@algo("use a balanced wrap algorithme")
def backtracking(words,width):
    words = list(words)
    count = len(words)
    if (count == 0):
        return [[]]
    breaks = [0] * (count+ 1)
    best_tmp = [0] * (count + 1)
    # do a greedy wrap to have some baseline score to work with,
    # else we'll end up with O(2^N) behavior
    best_score , breaks = greedy_wrap(words, count, width, breaks)

    (test,score_t)= balanced_wrap(words, breaks, best_tmp, count, width, best_score, 0, 0, 0)
    return show_wrap(words, count, breaks)
