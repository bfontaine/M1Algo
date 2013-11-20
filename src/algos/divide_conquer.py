# -*- coding: UTF-8 -*-
from .base import algo,justify

def divide(words, width):
	"""

	"""
	length_words = len(words)
	line = []
	if (length_words == 1 ):
		return (line,(words,len(words[0])))
	length_words2 = len(words) // 2
	if ((length_words2 *2) < length_words):
		words1 = words[:(length_words2+1)]
		words2 = words[(length_words2+1):]
	else:
		words1 = words[:length_words2]
		words2 = words[length_words2:]
	(lines1,(line1, l_length1)) = divide(words1,width)
	(lines2,(line2, l_length2)) = divide(words2,width)
	# parti f(n)
	if (lines2 == []):
		if ((l_length1+l_length2+1) < width):
			line1 = line1 + line2
			return (lines1, (line1, l_length1 + l_length2 + 1))
		else :
			lines1 = lines1 + [line1]
			return (lines1 ,(line2, l_length2))

	else:
		lines1 = lines1 + [line1]
		lines1 = lines1 + lines2
		return (lines1,(line2, l_length2))



@algo("")
def divide_conquer(words, width):
	"""
	This algorithm use a methode divide and conquer.
	At first divide
	[ [---------] ...   | [-------- ]  ]

	"""
	para = []
	words=[w for w in words]
	(lines, (word , l_length)) = divide(words, width)
	para = lines + [word]
	return para
