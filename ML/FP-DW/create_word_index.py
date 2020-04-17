import re

# Create list of words
document = 'During my few years as an ML/DS researcher and practitioner, there has been lots of ups and down, making many mistakes and finally finding out what would be the best way of doing a certain task. This is not only limited to coding or modeling choices but also how to approach a particular problem or deciding the most useful and realistic road map. In this story, I will try to summarize the highlights in both technical and roadmap. I am going to to start with code snippets of performing very common tasks in the best possible way I know and I will appreciate your comments to make sure we have the best possible one. I hope this will turn into a useful repository for better understanding of concepts and for elegant data science code. In particular, many of us are used to applying API from various libraries without really thinking how things done under the hood. I will start this journey by some small examples an see where the road will lead us.'
list_of_words = re.split('[.,]+\s*|\s+', document)

# Create 'word to index' and 'index to word' dictionaries
set_of_words = set(list_of_words)
num_of_words = len(set_of_words)
word_index = dict(zip(set_of_words, range(num_of_words)))
index_word = dict(zip(range(num_of_words), set_of_words))

print(word_index)
print(index_word)