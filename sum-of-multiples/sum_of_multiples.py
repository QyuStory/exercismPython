def sum_of_multiples(limit, multiples):
    lst = range(1, limit)
    result = []
    for elem in multiples:
        result += filter(lambda x: x%elem == 0, lst)
    result = set(result)
    return sum(result)
