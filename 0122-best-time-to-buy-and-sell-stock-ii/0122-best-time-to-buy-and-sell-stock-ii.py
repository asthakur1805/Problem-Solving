class Solution:

	def maxProfit(self, prices):

		resultProfit = 0

		buyPointer = 0

		for sellPointer in range(1, len(prices)):

			if prices[buyPointer] < prices[sellPointer]:

				resultProfit += (prices[sellPointer] - prices[buyPointer])

			buyPointer = sellPointer

		return resultProfit

				