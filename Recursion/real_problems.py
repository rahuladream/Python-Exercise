# We gonna solve the real problem now
"""
1. Power function problem
2. Factorial function
"""

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        res = num * factorial(num - 1)
        return res

def efun(num):
    if num == 0:
        return 1
    else:
        print(num * efun(num-2))
        return num * efun(num-2)

print("{} to the power of {} is {}".format(2,4, power(2,4)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
print("-------------SPECIAL ENTRY------------------")
print("efun: {} is {}".format(8, efun(8)))
