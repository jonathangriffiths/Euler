__author__ = 'Jono'

def sum(n):
    total = 0;
    for i in range(1, n+1):
        total+=i
    return total


def sumSquares(n):
    total = 0;
    for i in range(1, n+1):
        total+= (i**2)
    return total

print sum(100)**2 - sumSquares(100)