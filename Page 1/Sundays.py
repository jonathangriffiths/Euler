__author__ = 'Jono'

# info: 1 Jan 1900 was Monday

regular = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(n):
    if n % 4 == 0 and n % 100 !=0:
        return True
    elif n % 100 == 0 and n % 400 == 0:
        return True
    else:
        return False

def is_monday(days_passed):
    if days_passed % 7 == 0:
        return True
    else:
        return False

#In the 20th century (1901 - 2000) how many sundays fell on the first of a month?