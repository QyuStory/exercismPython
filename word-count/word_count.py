import re
from collections import Counter
def word_count(phrase):
    preprocess = list(map((lambda x: x.strip('\'')), 
                filter(                                         # filtering empty string
                    None, 
                    re.split('[^0-9a-z\']+', phrase.lower())    # convert lower case & split by non-numeralpha
                    )))

    return Counter(preprocess)                                  # groupby identity and (convert list to map)
