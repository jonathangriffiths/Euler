__author__ = 'Jono'

#iterative: n even --> n/2; n odd --> 3n+1
#ends at 1
#which number under 1,000,000 has longest chain

#Thoughts: whenever we hit an a number we know (3n+1 or n/2) can simply refer back to the known chain length

def max_length_collatz(n):
    #create list of numbers that need testing
    num_to_test = range(1,n+1)
    #create list of lengths for each number (i.e. position 0 is for 1, 200 is for 201 etc)
    terms_for_num = []
    for i in num_to_test:
        value = i
        terms = 1
        while value != 1:
            #if the value has already been calculated we can just add on the number of terms already found
            if value <= len(terms_for_num) :
                #minus 1 to remove the duplicated 1
                terms += (terms_for_num[value-1] - 1)
                break
            #Otherwise we just proceed to next term
            elif value % 2 == 0:
                value /= 2
                terms += 1
            elif value % 2 == 1:
                value = 3*value + 1
                terms += 1
        #Then we add the number of terms for the number to the list of answers
        terms_for_num.append(terms)
    #want to return the number with the most terms:
    return terms_for_num.index(max(terms_for_num))+1

print max_length_collatz(1000000)