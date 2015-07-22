
# Suppose you have a list of words and you want to sort them from longest to shortest:

txt = 'but soft what light in younder window breaks'
words = txt.split() # split txt by white space, return a list.
#print words
'''
The first loop builds a list of tuples, where each tuple is a word preceded by its length.
'''
t = list()
for word in words:
	t.append((len(word), word))
#print t
t.sort(reverse = True)
#print t
#for key, val in t:
	#print val, key
'''
The second loop traverses the list of tuples and builds a list of words in descending order of length.
'''
t1 = list()
for length, word in t:
	t1.append(word)
print t1
