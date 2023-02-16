class Solution:

	def maxProfit(self, prices):

		resultProfit = 0

		for sell in range(1, len(prices)):

			resultProfit += max(0, prices[sell]-prices[sell-1])

		return resultProfit