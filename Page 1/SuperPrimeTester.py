__author__ = 'Jono'
from numpy import sqrt

def is_prime(n):
    #speed improvements
    if n == 2 or n == 3 or n == 5:
        return True
    if n == 1:
        return False
    if n < 4:
        return True
    if n%2 == 0:
        return False
    if n<9:
        return False
    if n%3 == 0:
        return False
    #main part:
    limit = int(sqrt(n))
    counter = 5
    while counter <= limit:
        if n%counter == 0:
            return False
        if n % (counter+2) == 0:
            return False
        counter += 6
    return True