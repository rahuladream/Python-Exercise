"""
Best time to buy and sell stock

http://pythontutor.com/visualize.html#code=%22%22%22%0ABest%20time%20to%20buy%20and%20sell%20stock%0A%22%22%22%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20maxProfit%28self,%20prices%29%20-%3E%20int%3A%0A%20%20%20%20%20%20%20%20maxProfit%20%3D%200%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%281,%20len%28prices%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20prices%5Bi%5D%20%3E%20prices%5Bi%20-%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxProfit%20%2B%3D%20prices%5Bi%5D%20-%20prices%5Bi%20-%201%5D%0A%20%20%20%20%20%20%20%20return%20maxProfit%0A%0Aa%20%3D%20Solution%28%29%0Aprint%28a.maxProfit%28%5B7,1,5,3,6,4%5D%29%29&cumulative=false&curInstr=20&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""

class Solution:
	def maxProfit(self, prices) -> int:
		maxProfit = 0
		for i in range(1, len(prices)):
			if prices[i] > prices[i - 1]:
				maxProfit += prices[i] - prices[i - 1]
		return maxProfit

a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))