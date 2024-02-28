class Solution:

	def maxProfit(self,prices):

		secondPrev = [0]*2
		firstPrev = [0]*2

		for index in range(len(prices)-1,-1,-1):

			dp = [0]*2

			for canBuy in range(2):

				if canBuy:

					buy = -prices[index]+firstPrev[0]
					notBuy = firstPrev[1]

					dp[canBuy] = max(buy,notBuy)

				else:

					sell = prices[index]+secondPrev[1]
					notSell = firstPrev[0]

					dp[canBuy] = max(sell,notSell)

			secondPrev = firstPrev
			firstPrev = dp

		return firstPrev[1]

	