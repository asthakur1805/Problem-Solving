class Solution:

	def maxProfit(self, prices):

		resultProfit = 0

		for sellPointer in range(1, len(prices)):

			resultProfit += max(prices[sellPointer]-prices[sellPointer-1],0)

		return resultProfit