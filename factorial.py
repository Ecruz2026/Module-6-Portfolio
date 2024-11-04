
# Emmanuel Cruz 


#Oct 29, 2024

#his program calculates the factorial of a given number both by using a built-in math.factorial function and by manual calculation using a loop. It then checks whether both calculations are identical, while demonstrating some mathematical functions relating to the results.

import math


def factorial_manual(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


number = int(input("Enter a non-negative integer to calculate its factorial: "))


factorial_math = math.factorial(number)


factorial_manual_value = factorial_manual(number)


print(f"Factorial calculated using math.factorial: {factorial_math}")
print(f"Factorial calculated using a for loop: {factorial_manual_value}")


if factorial_math == factorial_manual_value:
    print("Both methods give the same result.")
else:
    print("The methods give different results!")


int_sqrt = math.isqrt(factorial_math)

ceil_value = math.ceil(1 / (factorial_manual_value if factorial_manual_value != 0 else 1))

print(f"The integer square root of the factorial is: {int_sqrt}")
print(f"The ceiling of 1/factorial is: {ceil_value}")