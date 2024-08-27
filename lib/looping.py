#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

# Test the function
happy_new_year()


def square_integers(int_list):
    return [x ** 2 for x in int_list]

# Test the function
print(square_integers([1, 2, 3, 4, 5]))  # [1, 4, 9, 16, 25]


def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Test the function
fizzbuzz()
