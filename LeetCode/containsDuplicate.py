"""
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct

http://pythontutor.com/visualize.html#code=%22%22%22%0AYour%20function%20should%20return%20true%20if%20any%20value%20appears%20at%20least%20twice%20in%20the%20array,%20and%20it%20should%20return%20false%20if%20every%20element%20is%20distinct%0A%22%22%22%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20containsDuplicate%28self,%20nums%29%20-%3E%20bool%3A%0A%20%20%20%20%20%20%20%20newList%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums%29%20-%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20nums%5Bi%5D%20%3D%3D%20nums%5Bi%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0Aa%20%3D%20Solution%28%29%0Aprint%28a.containsDuplicate%28%5B1,1,1,3,3,4,3,2,4,2%5D%29%29&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""

class Solution:
	def containsDuplicate(self, nums) -> bool:
		newList = []
		for i in range(len(nums) - 1):
			if nums[i] == nums[i + 1]:
				return True
			else:
				return False

a = Solution()
print(a.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))