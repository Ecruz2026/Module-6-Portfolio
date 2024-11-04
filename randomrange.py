
# Emmanuel Cruz 


#Oct 29, 2024

# This program generates and prints 10 random integers between 25 and 35, storing each of those integers in a list called 'rand_nums.'

import random

rand_nums = []

for _ in range (10):
    num = random.randrange (25, 36)
    rand_nums.append(num)
    print (num)
    print ("List of random numbers:", rand_nums)