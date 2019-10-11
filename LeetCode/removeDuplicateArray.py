"""
Given sorted array remove the duplicates in-place such that each element appear only once and return new length
"""

class Solution:
	def removeDuplicates(self, nums) -> int:
		# newList = list(dict.fromkeys(nums))
		# newLen = len(newList)
		newList = []
		for val in nums:
			if val not in newList:
				newList.append(val)
		return len(newList)


if __name__ == '__main__':
	a = Solution()
	print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
	