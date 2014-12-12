__author__ = 'Jono'

from GetPrimeN import isPrime


#basic method to estimate how long it will take like this
def get_sum_primes_below_n(n):
    sum=2
    for i in range(3, n+1, 2):
        if isPrime(i):
            sum+=i
    return sum



print get_sum_primes_below_n(2000000)

#note: Erastosthenes seive useful for speed
#1. Make a list of all numbers from 2 to N.
#2. Find the next number p not yet crossed out. This is a prime. If it is greater than √N, go to 5.
#3. Cross out all multiples of p which are not yet crossed out.
#4. Go to 2.
#5. The numbers not crossed out are the primes not exceeding N
