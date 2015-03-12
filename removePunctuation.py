import string
import sys

file = open('file.txt','r')
review = file.read()
file.close()
for punct in string.punctuation:
	review.replace(punct,"")
words=review.split(" ")
print words
