# encoding:utf-8

def break_words(stuff):
	"""This function will break up words for us."""
	
	words = stuff.split(' ')
	
	return words
	
def sort_words(words):
	"""Sorts the words."""
	
	return sorted(words)

def print_first_word(words):
	
	"""Print the first word after poping it off. """
	
	word = word.pop(0)
	
	print word
	
def print_last_word(words):
	"""Print the last word after poping it off."""
	
	word = words.pop(-1)
	
	print word
	
def sort_sentence(sentence):

	words = break_words(sentence)

	return sort_words(words)
	


