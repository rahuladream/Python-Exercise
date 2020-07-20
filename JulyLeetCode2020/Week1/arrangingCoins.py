

class Solution:
    def arrangeCoins(self, n):
        """ Some code
        Using general maths
        """
        row = 0
        if n == 1 or n == 0:
            return n
        for num in range(1,n+1):
            row += 1 
            n -= num
            if n < 0:
                return row - 1
            

class Solution2:
    def arrangeCoins(self, n):
        """ Using binary search """
        l, r = 0, n
        while l <= r:
            k = (r + l) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                r = k - 1
            else:
                l = k + 1
        return r



if __name__ == '__main__':
    obj = Solution()
    print(obj.arrangeCoins(8))

    obj2 = Solution2()
    print(obj2.arrangeCoins(8))
