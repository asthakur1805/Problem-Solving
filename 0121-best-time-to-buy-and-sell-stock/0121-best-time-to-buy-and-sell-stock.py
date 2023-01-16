class Solution:

	def maxProfit(self, prices):

		buyPointer = 0

		resultProfit = 0

		for sellPointer in range(1, len(prices)):

			if prices[sellPointer] < prices[buyPointer]:

				buyPointer = sellPointer

			else:

				resultProfit = max(resultProfit, prices[sellPointer]-prices[buyPointer])


		return resultProfit
					