"""
Recursion is function that call itself

In this example creating code to count down till given data
"""


def countdown(x):
    if (x == 0):
        print("Completed")
    else:
        print(x)
        countdown(x-1)
        # what happen to the down code
        print("bar..")
        # The function will return to The
        # original stack that means it will
        # run 5 times to return original stack
countdown(15)
