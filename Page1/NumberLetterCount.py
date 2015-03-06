__author__ = 'Jono'

def decide_digit_length(n):
    try:
        if n == 1 or n == 2 or n == 6:
            return 3
        if n == 4 or n == 5 or n == 9:
            return 4
        if n == 3 or n == 7 or n == 8:
            return 5
        if n == 0:
            return 0
    except:
        print 'Oh no!'

def decide_teens_length(n):
    if n == 17:
        return 9
    if n == 10:
        return 3
    if n == 11 or n == 12:
        return 6
    if n == 15 or n == 16:
        return 7
    if n == 13 or n == 18 or n == 14 or n == 19:
        return 8

def decide_length(n):
    #note only up to 99
    if n < 10:
        return decide_digit_length(n)
    if n < 20:
        return decide_teens_length(n)
    first_digit = int(str(n)[0])  # this is the tens
    second_digit = int(str(n)[1])  # this is the ones
    # Now we can just do the length of e.g. twenty plus the length of e.g. two
    if first_digit < 4 or first_digit > 7:
        return 6 + decide_digit_length(second_digit)
    if first_digit < 7:
        return 5 + decide_digit_length(second_digit)
    if first_digit == 7:
        return 7 + decide_digit_length(second_digit)

count=0
# for one to one thousand
# the hundreds, each 'n hundred' is repeated one hundred times
for i in range(1, 10):
    count += 100 * (7 + decide_digit_length(i))

# the thousand
count += 11

# now to deal with one to 99
for i in range(1, 100):
    count += 10 * (decide_length(i))  # loops ten times to 1000

# finally the ands
# all of them have an and except the first 100 (incl 100), 8 other hundreds exactly and 1000
count += 3 * (1000 - 100 - 8 - 1)

print count