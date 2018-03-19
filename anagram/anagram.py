from collections import Counter

def create_lh_dic(word):
    return Counter(list(word[0].lower()+word[1:]))

def detect_anagrams(word, candidates):
    dic = create_lh_dic(word)
    anagrams = []
    for elem in candidates:
        if dic == create_lh_dic(elem):
            anagrams.append(elem)
    return anagrams
