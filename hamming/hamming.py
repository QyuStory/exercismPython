def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) is not len(strand_b):
        raise ValueError("difference of length error")
    for a, b in zip(strand_a, strand_b):
        if a is not b:
            count += 1
    return count
