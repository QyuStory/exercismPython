def is_digit(num):
    try:
        int(num)
    except ValueError:
        return False
    return True

def decode(string):
    count, result = '', ''
    for e in string:
        if is_digit(e):
            count += e
        else:
            result += e
            if not count:
                pass
            else:
                for i in range(int(count)-1):
                    result += e
            count = ''
    return result

def encode(string):
    temp, result = '', ''
    count = 0
    for elem in string+'\n':
        if temp is elem:
            count += 1
        elif not temp:
            temp = elem
            count = 1
        else:
            if count is 1:
                result += temp
            else:
                result += str(count) + temp
            temp = elem
            count = 1
    return result
