class Solution:

	def maxProfit(self, prices):

		resultProfit = 0

		for sell in range(1, len(prices)):

			resultProfit += max(prices[sell]-prices[sell-1], 0)

		return resultProfit