class Solution:

	def maxProfit(self,prices):

		dp = [[[0]*3 for _ in range(2)] for _ in range(len(prices)+1)]

		for index in range(len(prices)-1,-1,-1):

			for canBuy in (0,1):

				for maxTransactions in (1,2):

					if canBuy:

						buy = -prices[index]+dp[index+1][0][maxTransactions]
						notBuy = dp[index+1][1][maxTransactions]

						dp[index][canBuy][maxTransactions] = max(buy,notBuy)

					else:

						sell = prices[index]+dp[index+1][1][maxTransactions-1]
						notSell = dp[index+1][0][maxTransactions]
	
						dp[index][canBuy][maxTransactions] = max(sell,notSell)

		return dp[0][1][2]