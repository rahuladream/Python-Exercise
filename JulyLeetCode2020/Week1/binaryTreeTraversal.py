

class Solution:
    
    def levelOrderButtom(self, root):
        """
        Code
        """
        tmp = []
        self.recursive(root, 0, tmp)
        return tmp
    
    def recursive(self, root, depth, tmp):
        if root:
            if depth >= len(tmp):
                tmp.insert(0, [])
            tmp[-(depth + 1)].append(root.val)
            self.recursive(root.left, depth + 1, tmp)
            self.recursive(root.right, depth + 1, tmp)




if __name__ == '__main__':
    obj = Solution()
    print(obj.levelOrderButtom([3,9,20,None,None,15,7]))