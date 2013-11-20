# -*- coding: UTF-8 -*-
from .base import algo,justify

def divide(words, width):
	"""

	"""
	length_words = len(words)
	line = []
	if (length_words == 1 ):
		return (line,(words,len(words[0])))
	length_words = len(words) // 2
	c1 = divide(words[:length_words],w)
	c2 = divide(words[length_words:],w)
	# parti f(n)
	c1 =(lines1, (line1, l_length1))
	c2 =(lines2, (line2, l_length2))
	if (lines2 == []):
		if (l_length1 == 0):
			return (lines1, (line2, l_length))
		else if ((l_length1+l_length2+1) < width):
			return (lines1, ((line1 + line2), l_length1 + l_length2 + 1))
		else :
			return (lines1 +line1 ,(line2, l_length2))

	else:
		if (l_length1 == 0):
			return (lines1 + lines2 ,(line2, l_length2))
		else:
			return (lines1 + line1 + lines2 ,(line2, l_length2))



@algo("")
def divide_conquer(words, width):
	"""
	This algorithm use a methode divide and conquer.
	At first divide
	[ [---------] ...   | [-------- ]  ]

	"""
	para = []
	words=[w for w in words]
	dico = divide(words, width)
	dico = (lines, (word , l_lenght))
	if (l_length > 0):
		para = lines + word
	else :
		para = lines
	return para
