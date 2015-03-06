__author__ = 'Jono'

from numpy import sqrt

def is_pythag_triple(a,b,c):
    if (a**2 + b**2) == c**2:
        return True
    else:
        return False

#will find a pythagorean triple where a+b+c=n
def find_pythag_triple_product_given_sum(sum):
    #define hyp>adj>opp to save some looping - makes method much faster
    for opposite in range(1, sum):
        if opposite%10==0:
            print 'got through '+str(opposite)+' opposite values'
        for adjacent in range(opposite, sum):
            for hypotenuse in range(adjacent, sum):
                if is_pythag_triple(opposite, adjacent, hypotenuse) and opposite+adjacent+hypotenuse==sum:
                    return opposite*hypotenuse*adjacent

#much better to use maths and remove a loop:
#sub out c
def alternative_method(sum):
    for opposite in range(1, sum):
        for adjacent in range(opposite, sum):
            if (1000-opposite-adjacent)==sqrt(adjacent**2 + opposite**2):
                    return opposite*adjacent*sqrt(adjacent**2 + opposite**2)

    
print alternative_method(1000)
#print find_pythag_triple_product_given_sum(1000)
