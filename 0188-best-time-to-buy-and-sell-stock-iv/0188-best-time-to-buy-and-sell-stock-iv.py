class Solution:

	def maxProfit(self,k,prices):

		prev = [[0]*(k+1) for _ in range(2)]

		for index in range(len(prices)-1,-1,-1):

			dp = [[0]*(k+1) for _ in range(2)]

			for canBuy in range(2):

				for maxTransactions in range(1,k+1):

					if canBuy:

						buy = -prices[index]+prev[0][maxTransactions]
						notBuy = prev[1][maxTransactions]

						dp[canBuy][maxTransactions] = max(buy,notBuy)

					else:

						sell = prices[index]+prev[1][maxTransactions-1]
						notSell = prev[0][maxTransactions]

						dp[canBuy][maxTransactions] = max(sell,notSell)

			prev = dp

		return prev[1][k]
