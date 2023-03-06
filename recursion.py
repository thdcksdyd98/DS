# call stack

def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne() 

# ->
# Three
# Two
# One

# CALL STACK:
# funcThree -> first
# funcTwo -> second
# funcOne -> third

# recursion - factorial 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)