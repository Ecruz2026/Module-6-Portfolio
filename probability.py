
# Emmanuel Cruz 


#Oct 29, 2024

# This program simulates flipping a biased coin 1,000 times, showing "heads" 85% of the time and "tails" 15% of the time, while storing each result in a list and calculating the actual percentage of heads in the results.



import random

X = 85
flips = 1000

results = []

for _ in range(flips):
    if random.randint(1, 100) <= X:
        results.append("heads")
    else:
        results.append("tails")

        heads_count = results.count("heads")
heads_percentage = (heads_count / flips) * 100

print(f"Out of {flips} flips:")
print(f"Heads: {heads_count} times ({heads_percentage:.2f}%)")
print(f"Tails: {flips - heads_count} times ({100 - heads_percentage:.2f}%)")
