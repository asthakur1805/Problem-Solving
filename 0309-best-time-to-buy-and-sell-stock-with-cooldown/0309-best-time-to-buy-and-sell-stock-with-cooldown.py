class Solution:

	def maxProfit(self,prices):

		dp = [[0]*2 for _ in range(len(prices)+2)]

		for index in range(len(prices)-1,-1,-1):

			for canBuy in range(2):

				if canBuy:

					buy = -prices[index]+dp[index+1][0]
					notBuy = dp[index+1][1]

					dp[index][canBuy] = max(buy,notBuy)

				else:

					sell = prices[index]+dp[index+2][1]
					notSell = dp[index+1][0]

					dp[index][canBuy] = max(sell,notSell)

		return dp[0][1]
