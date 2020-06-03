# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x #says to use global variable x and change it to 99
    x = 99
    #print(x) #prints local variable x=99
change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?



print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y #this makes the func use a nonlocal ie global y
        y = 999

    inner() #moved the location to the inside of inner function

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
