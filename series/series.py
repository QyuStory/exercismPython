def slices(series, length):
    if len(series) < length or length is 0:
        raise ValueError("length not matched")
    else:
        temp = [series[i:i+length] for i in range(len(series) - length + 1)]
        preInt = [list(x) for x in temp]
        returnVal = []
        for elem in preInt:
            returnVal.append(list(map(int, elem)))
        return returnVal
