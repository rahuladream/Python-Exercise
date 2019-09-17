# We gonna solve the real problem now
"""
1. Power function problem
2. Factorial function
"""

def power(num, pwr):
    return (num ** pwr)


def factorial(num):
    if (num == 0):
        return None
    else:
        res = num * (num - 1)
        return res


print("{} to the power of {} is {}".format(2,4, power(2,4)))
print("{}! is {}".format(4, factorial(4)))
