import re
def is_pangram(sentence):
    preprocess = re.sub('[0-9_ ."]', '', sentence.lower())
    return len(set(preprocess)) == 26
