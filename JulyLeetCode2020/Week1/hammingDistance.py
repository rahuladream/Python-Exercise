#!/bin/python

'''
Hamming Distance -

the Distance between two integers is the number of positions
at which the corresponding bits are different.

1 (0 0 0 1)
4 (0 1 0 0)
     w   w

answer is 2
'''

class Solution:
    def hammingDistance(self, x, y):
        xbits = "{0:032b}".format(x)
        ybits = "{0:032b}".format(y)
        count = 0
        print(xbits, ybits)
        for i in range(0, len(xbits)):
            if xbits[i] != ybits[i]:
                count += 1
        return count



if __name__ == '__main__':
    obj = Solution()
    print(obj.hammingDistance(680142203, 1111953568))


