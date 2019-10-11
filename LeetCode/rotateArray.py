"""
Rotate the array to the right by k steps, where is non-negative
"""

class Solution:
	def rotate(self, nums, k) -> None:
		if k > len(nums):
			k = k//len(nums)
		return nums[-k:] + nums[:-k]

a = Solution()
print(a.rotate([-1,-100,3,99], 2)) 