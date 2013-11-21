# -*- coding: UTF-8 -*-
from .base import algo,justify

def f1(words,width):
	length_words = len(words)
	if(length_words == 1):
		return ([], (words, len(words[0])))
	k_n = words[:(length_words -1)]
	(line, (current_line, length)) = f1(k_n, width)
	w = words[length_words -1]
	l_w = len(w)
	if ((length + l_w + 1) <= width):
		return (line ,(current_line + [w], length + l_w +1))
	else:
		return (line + [current_line], ([w] ,l_w))

@algo("")
def recursive(words, width):
	"""
	"""
	words=[w for w in words]
	length_words = len(words)
	(line,(current_line,l_length)) = f1(words , width)
	line = line + [current_line]
	return line
