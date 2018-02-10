import re
def is_isogram(string):
    preprocess = re.sub('[- .]', '', string.lower())
    return len(preprocess) == len(set(preprocess))
