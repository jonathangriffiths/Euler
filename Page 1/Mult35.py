__author__ = 'Jono'


def sum(max_number):
    total = 0
    for n in range(1, max_number):
        if n%3==0:
            total+=n
        elif n%5==0:
            total+=n
    return total

print sum(1000)