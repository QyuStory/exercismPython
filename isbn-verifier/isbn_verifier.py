def is_digit(g):
    try:
        float(g)
    except ValueError:
        return False
    return True

def verify(isbn):
    intrinsic = isbn.replace('-', '')
    if not intrinsic or len(intrinsic) > 10: # empty or too long
        return False
    front, tail = intrinsic[0:9], intrinsic[-1]
#    if all(is_digit(x) for x in front) and (tail.isdigit or tail is 'X'):
    if all(is_digit(x) for x in front):
        if tail is 'X':
            return (sum(list(int(x)*y for x, y in zip(front, range(10, 1, -1)))) + 10) % 11 == 0
        else:
            try:
                return (sum(list(int(x)*y for x, y in zip(front, range(10, 1, -1)))) + int(tail)) % 11 == 0
            except ValueError:
                return False
    else:
        return False
