import re
def abbreviate(words):
    result = []
    lst = re.split('\s|-', words)
    for elm in lst:
        result += elm[0].upper()
    return ''.join(result)
