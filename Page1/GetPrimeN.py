__author__ = 'Jono'

import numpy

def isPrime(n):
    #speed improvements
    if n==2 or n==3 or n==5:
        return True
    if n%2 == 0 or n%3 == 0 or n%5 ==0:
        return False
    #main part:
    for i in range(2, int(numpy.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


def getNthPrime(N):
    run=True
    primes_found = 0
    testing=2
    while run == True:
        if isPrime(testing):
            primes_found+=1
            prime = testing
            testing+=1
        else:
            testing+=1
        if primes_found==N:
            return prime

print getNthPrime(10001)