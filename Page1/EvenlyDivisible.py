__author__ = 'Jono'



def evenlyDivisible(number, max_factor):
    #bottom half are just mirrors of the top half
    #(2*n is also divisible by n)
    factors_for_test = range(max_factor, max_factor/2, -1)
    for i in factors_for_test:
        if number%i != 0:
            return False
    return True

run=True
test=20

while run==True:
    #must be divisible by 20 so can just add 20s
    test+=20
    if evenlyDivisible(test, 20):
        run = False
        print test

