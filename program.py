# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

for number in range(1, 33):
    if number % fizzbuzz == 0:
        print("FizzBuzz")
    elif number % fizz == 0:
        print("Fizz")
    elif number % buzz == 0:
        print("Buzz")
    else:
        print(number)