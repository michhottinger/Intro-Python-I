# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE

def f1(x, y):
    return x + y

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE

def f2(*args):
    return sum(args)


print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?


def f2(*args):
    o = []
    for arg in args: 
        o = sum(arg)
    return o

print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE

def f3(a, b=None):
    return a+b if b is not None else a+1

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE

def f4(**attributes):
    """Return a string of comma-separated key-value pairs. key: foo, value: bar"""
    return ",".join(
        f"key: {param}, value: {value}"
        for param, value in attributes.items()
    )

# Should print
# key: a, value: 12
# key: b, value: 30
print(f4(a=12, b=30)) #does not print on separtate lines--havent' found how to do this in f-string

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
print(f4(city="Berkeley", population=121240, founded="March 23, 1868"))

d = {
    "monster": "goblin",
    "hp": 3
}


def f4(dict):
    """Return a string of comma-separated key-value pairs. key: foo, value: bar"""
    return ",".join(
        f"key: {param}, value: {value}"
        for param, value in dict.items()
    )


# How do you have to modify the f4 call below to make this work?
print(f4(d))
