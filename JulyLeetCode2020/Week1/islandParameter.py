class Solution:

    def islandParameter(self, grid):
        '''

        '''
        area = 0
        for row in grid + list(map(list, zip(*grid))):
            for i1, i2 in zip([0] + row, row + [0]):
                area += int(i1 != i2)
        return area
    

if __name__ == '__main__':
    obj = Solution()
    print(obj.islandParameter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]))