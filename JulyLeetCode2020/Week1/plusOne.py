class Solution:
    def plusOne(self, digits):
        '''
        Given a non-empty array of digits representing
        a non-negative integer, increment one to the
        integer
        '''
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits 

if __name__ == '__main__':
    obj = Solution()
    print(obj.plusOne([1,2,9]))