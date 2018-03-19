import re

def is_blank(phrase):
    if phrase and phrase.strip():
        return False
    return True

def is_question(phrase):
    preprocess = re.sub('[^0-9a-zA-Z?]', '', phrase)
    if preprocess.endswith('?'):
        return True
    else:
        return False

def is_yelling(phrase):
    if (re.sub('[\W]', '', phrase)).isupper():
        return True
    else:
        return False

def hey(phrase):
    if is_yelling(phrase) and is_question(phrase):
        return 'Calm down, I know what I\'m doing!'
    elif is_question(phrase):
        return 'Sure.'
    elif is_yelling(phrase):
        return 'Whoa, chill out!'
    elif is_blank(phrase):
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
