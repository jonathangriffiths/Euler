__author__ = 'Jono'

huge_number = 2**1000
huge_string = str(huge_number)

counter = 0

for i in range(1, len(huge_string)+1):
    counter += int(huge_string[i-1])

print counter