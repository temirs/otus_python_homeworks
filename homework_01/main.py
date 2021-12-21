import math


def power_numbers(*my_list):
    return [i ** 2 for i in my_list]


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(lst):
    d = []
    for i in lst:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                break
            j += 1
        else:
            if i > 1:
                d.append(i)
    return d


def is_odd(lst):
    return [i for i in lst if i % 2 != 0]


def is_even(lst):
    return [i for i in lst if i % 2 == 0]


def filter_numbers(lst, func):

    if func == ODD:
        return is_odd(lst)
    elif func == EVEN:
        return is_even(lst)
    elif func == PRIME:
        return is_prime(lst)
