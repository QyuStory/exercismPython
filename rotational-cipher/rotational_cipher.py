def shift_by_key(ch, key):
    if ord(ch) + key > ord('z'):
        return chr((ord(ch) + key)%ord('z') + ord('a') - 1)
    else:
        return chr(ord(ch) + key)

def rotate(text, key):
    accum = ''
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                accum += shift_by_key(ch.lower(), key).capitalize()
            else:   
                accum += shift_by_key(ch, key)
        else:
            accum += ch
    return accum
