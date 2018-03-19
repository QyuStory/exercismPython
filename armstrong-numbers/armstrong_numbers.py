def is_armstrong(number):
    string = str(number)
    length = len(string)
    accum = 0
    for x in string:
        accum += int(x) ** length
    return accum == number
