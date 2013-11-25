# -*- coding: UTF-8 -*-
from .base import algo

def carre(n):
	return n*n

def cube(n):
	return n*n*n

def retsoluce(words, lines, n):
	if (lines[n] == 1):
		line = []
		for i in range (lines[n],n+1):
			line = line + [words[i-1]]
		return ([line],[])
	else :
		(para,line) = retsoluce(words, lines, lines[n]-1)
	for i in range (lines[n],n+1):
		line = line + [words[i-1]]
	return (para + [line],[])

def WordsWrap(len_word, n , Width, func = carre):
	INF = 100000
	# lc[i][j] will have cost of a line which has words from i to j
	lc = [[0 for i in range(0,(n+1))] for j in range(0,(n+1))]
	# c[i] will have total cost of optimal arrangement of words 
	# form 1 to i
	c = [0 for i in range(0,n+1)]
	# line is used to return solution
	line = [0 for i in range(0,n+1)]
	# calculate extra spaces in a single line.  The value lc[i][j]
	# indicates extra spaces if words from word number i to j are
	# placed in a single line
	for i in range(1,n+1):
		lc[i][i] = Width - len_word[i-1]
		for j in range(i+1,n+1):
			lc[i][j] = lc[i][j-1] - len_word[j-1] - 1
		# Calculate line cost corresponding to the above calculated extra spaces.
		# The value lc[i][j] indicates cost of putting words from word 
		# number i to j in a single line
		for j in range(i,n+1):
			if (lc[i][j] < 0):
				lc[i][j] = INF
			elif ((j == n) and (lc[i][j] <= 0)):
				lc[i][j] = 0
			else :
				lc[i][j] = func(lc[i][j])
	# Calculate line cost corresponding to the above calculated extra
	# spaces. The value lc[i][j] indicates cost of putting words from
	# word number i to j in a single line
	c[0]=0
	for j in range(1,n+1):
		c[j]= INF
		for i in range(1,j+1):
			if((c[i-1] != INF)\
				and (lc[i][j] != INF )\
				and  ((c[i-1] + lc[i][j]) < c[j])):
				c[j] = c[i-1] + lc[i][j]
				line[j] = i
	return line

@algo("A dynamic programming use methode word wrap to knuth with function square")
def dynamic_carre(words , width):
	words=[w for w in words]
	len_words = len(words)
	l = [len(w) for w in words]
	lines = WordsWrap(l , len_words, width, carre)
	(para,line_words) = retsoluce(words, lines, len_words)
	return para

@algo("A dynamic programming use methode word wrap to knuth with function cube")
def dynamic_cube(words , width):
	words=[w for w in words]
	len_words = len(words)
	l = [len(w) for w in words]
	lines = WordsWrap(l , len_words, width, cube)
	(para,line_words) = retsoluce(words, lines, len_words)
	return para
