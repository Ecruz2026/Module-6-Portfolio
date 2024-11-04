
# Emmanuel Cruz 


#Oct 29, 2024

# This program randomly picks a day of the week from a list and prints a message that describes a rainy day with lightning for that specific day.



import random
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random_day = random.choice(days_of_week)
print(f"It was a rainy {random_day} and the lightning flashed across the sky.")