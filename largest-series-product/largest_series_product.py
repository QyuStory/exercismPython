def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

def largest_product(series, size):
    if size < 0:
        raise ValueError('The size must be a positive number')
    else:
        lst = [series[i:i+size] for i in range(len(series)-size+1)]
        ad_split = [list(x) for x in lst]
        to_int = [list(map(int, ad_split[i])) for i in range(len(ad_split))]
        mult_each_elem = [multiply(to_int[i]) for i in range(len(to_int))]
        return max(mult_each_elem)
