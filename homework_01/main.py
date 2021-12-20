import math

def power_numbers(*list):
    return [i ** 2 for i in list]


ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(list):
    d = []
    for i in list:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
        else:
            if i > 1:
                d.append(i)
    return d


def filter_numbers(list, func):

    def ODD(list):
        return [i for i in list if i % 2 != 0]

    def EVEN(list):
        return [i for i in list if i % 2 == 0]

    if func == 'odd':
        return ODD(list)
    elif func == 'even':
        return EVEN(list)
    elif func == 'prime':
        return is_prime(list)
