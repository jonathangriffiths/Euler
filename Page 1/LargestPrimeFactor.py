__author__ = 'Jono'

import numpy as np


def isPrime(number):
    if number == 1 or number%2 == 0:
        return False
    for i in range(3, int(np.sqrt(number))):
        if number%i == 0:
            return False
    return True


def largestPrimeFactor(number):
    count_to = np.sqrt(number)
    for i in range(3, int(count_to)):
        if number%i==0 and isPrime(i):
            largest_prime = i
    return largest_prime

print largestPrimeFactor(600851475143)