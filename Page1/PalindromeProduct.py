__author__ = 'Jono'

def isPalindrome(number):
    string = str(number)
    #Even/odd makes no difference as the .5 is dropped
    for i in range(0, len(string)/2):
        if string[i] != string[-(i+1)]:
            return False
    return True

def testPalindrome(order_of_mag):
    largest_product=1
    for i in range(1, 10**order_of_mag):
        for j in range(1, 10**order_of_mag):
            product = i*j
            if isPalindrome(product) and product>largest_product:
                largest_product = product
    return largest_product

print testPalindrome(3)