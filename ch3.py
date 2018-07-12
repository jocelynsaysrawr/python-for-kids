# The Calculator
#
# 1. The calculator needs power.
# 2. The user enters the first number.
# 3. The user presses and operation key (+, -, *, or /).
# 4. The user enters a second number.
# 5. The user presses the = key.
# 6. Then, an answer is printed to the screen.

# Write a function to add two numbers together.


def addition():
    first_number = float(
        input('I will add two numbers. Enter the first number: '))
    second_number = float(input('Now enter the second number: '))
    print(first_number + second_number)


addition()

# Write a function to subtract one number from another number.


def subtraction():
    first_number = float(input(
        'I will subtract one number from another number. Enter the first number: '))
    second_number = float(input('Now enter the second number: '))
    print(first_number - second_number)


subtraction()

# Write a function to multiply two numbers.


def multiplication():
    first_number = float(
        input('I will multiply two numbers. Enter the first number: '))
    secont_number = float(input('Now enter the second number: '))
    print(first_number * secont_number)


multiplication()

# Write a function to divide two numbers.


def division():
    first_number = float(
        input('I will divide two numbers. Enter the first number: '))
    second_number = float(input('Now enter the second number: '))
    print(first_number / second_number)


division()

# Write a function to find the remainder after division.


def modulo():
    first_number = float(input(
        'I will find the remainder after dividing two numbers. Enter the first number: '))
    second_number = float(input('Now enter the second number: '))
    print(first_number % second_number)


modulo()
