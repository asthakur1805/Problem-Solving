class Solution:

	def maxProfit(self,prices):

		prev = [[0]*3 for _ in range(2)]

		for index in range(len(prices)-1,-1,-1):

			dp = [[0]*3 for _ in range(2)]

			for canBuy in (0,1):

				for maxTransactions in (1,2):

					if canBuy:

						buy = -prices[index]+prev[0][maxTransactions]
						notBuy = prev[1][maxTransactions]

						dp[canBuy][maxTransactions] = max(buy,notBuy)

					else:

						sell = prices[index]+prev[1][maxTransactions-1]
						notSell = prev[0][maxTransactions]
	
						dp[canBuy][maxTransactions] = max(sell,notSell)

			prev = dp

		return prev[1][2]