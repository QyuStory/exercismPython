def sieve(limit):
    test_member = [x for x in range(2, limit+1)]
    result = []
    for prime in test_member:
        if all(prime%divider for divider in test_member if prime is not divider):
            result.append(prime)
    return result
