import string

def convert(ch):
    return chr(ord('a') + (25 + (ord('a') - ord(ch))))

def preprocess(text, isEncode):
    count = 0
    lwrNDelSp = text.lower().replace(' ','')
    filt = ''.join(filter(lambda x: x.isalnum(), lwrNDelSp))
    result = ''
    for x in filt:
        if x.isdigit():
            result += x
            count += 1
        elif count > 4 and isEncode:
            result += ' ' + convert(x)
            count = 1
        else:
            result += convert(x)
            count += 1
    return result

def encode(plain_text):
    return preprocess(plain_text, True)


def decode(ciphered_text):
    return preprocess(ciphered_text, False)
