def find_gcd_euclidean(a,b):
    """Find GCD using Euclidean algorithm, a,b > 0"""
    while b:
        a, b = b, a % b
    return a

def count_frequency(lst):
    """Count frequency of elements in a list and return as a dictionary"""
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq