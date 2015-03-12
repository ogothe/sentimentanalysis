import string
import sys

file = open('file.txt','r')
review = file.read()
for punct in string.punctuation:
	review.replace(punct,"")
words=text.split(" ")
print words
