class Solution:

	def maxProfit(self, prices):

		buy, resultProfit = 0, 0

		for sell in range(1, len(prices)):

			if prices[buy] > prices[sell]:

				buy = sell

			else:

				resultProfit = max(resultProfit, prices[sell]-prices[buy])

		return resultProfit