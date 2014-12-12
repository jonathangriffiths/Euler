__author__ = 'Jono'

def getEvenFibSum(max_number):
    a = 1
    b = 1
    sum=0
    while a <= max_number and b <= max_number:
        new_term = a + b
        a = new_term
        new_term = a + b
        b = new_term
        if a%2 == 0:
            sum+=a
        if b%2 == 0:
            sum+=b
    return sum

print getEvenFibSum(4000000)