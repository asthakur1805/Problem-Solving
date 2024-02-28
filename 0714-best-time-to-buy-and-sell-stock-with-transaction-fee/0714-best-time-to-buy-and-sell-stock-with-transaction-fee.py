class Solution:

	def maxProfit(self,prices,fee):

		prev = [0]*2

		for index in range(len(prices)-1,-1,-1):

			dp = [0]*2

			for canBuy in range(2):

				if canBuy:

					buy = -prices[index]+prev[0]
					notBuy = prev[1]

					dp[canBuy] = max(buy,notBuy)

				else:

					sell = prices[index]-fee+prev[1]
					notSell = prev[0]

					dp[canBuy] = max(sell,notSell)

			prev = dp

		return prev[1]
