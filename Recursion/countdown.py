"""
Recursion is function that call itself

In this example creating code to count down till given data
"""


def countdown(x):
    if (x == 0):
        print("Completed")
    else:
        print(x)
        return countdown(x-1)

countdown(5)
