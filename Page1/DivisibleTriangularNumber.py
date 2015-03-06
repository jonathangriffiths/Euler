__author__ = 'Jono'
from numpy import sqrt


def get_nth_triangular_number(n):
    return sum(range(1, n+1))


def is_in_list(number, list):
    for i in list:
        if i==number:
            return True
    return False




def get_factors(n):
    small_factors=[]
    #populate up to the highest prime factor
    for i in range(1, int(sqrt(n))+2):
        if n%i==0:
            small_factors.append(i)
    #now make up the other factors using multiples
    #loop through each factor and make multiples by each other factor...
    factors = list(small_factors)
    for j in small_factors:
        for k in small_factors:
            temp_factor = j*k
            #if it works and is not there then:
            if n%temp_factor==0 and not is_in_list(temp_factor, factors):
                factors.append(temp_factor)
    if not is_in_list(n, factors):
        factors.append(n)
    return factors


def triangular_number_with_n_factors(n):
    unsolved = True
    i=1
    while unsolved:
        number_to_test = get_nth_triangular_number(i)
        if len(get_factors(number_to_test))>=n:
            unsolved=False
        else:
            i+=1
    return number_to_test

print triangular_number_with_n_factors(500)

#little comment to test git
