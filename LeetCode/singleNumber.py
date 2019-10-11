"""
Non-empty array of integers, every element appears twice except for one. Find that single one.

http://pythontutor.com/visualize.html#code=%22%22%22%0ANon-empty%20array%20of%20integers,%20every%20element%20appears%20twice%20except%20for%20one.%20Find%20that%20single%20one.%0A%22%22%22%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20singleNumber%28self,%20nums%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20newList%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20i%20in%20nums%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20not%20in%20newList%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20newList.append%28i%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20newList.remove%28i%29%0A%20%20%20%20%20%20%20%20return%20newList.pop%28%29%0A%0Aa%20%3D%20Solution%28%29%0Aprint%28a.singleNumber%28%5B4,1,2,1,2%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

"""

class Solution:
	def singleNumber(self, nums) -> int:
		newList = []
		for i in nums:
			if i not in newList:
				newList.append(i)
			else:
				newList.remove(i)
		return newList.pop()

a = Solution()
print(a.singleNumber([4,1,2,1,2])) 