class Solution:

	def change(self,amount,coins):

		dp = [[0]*(amount+1) for _ in range(len(coins))]

		for currAmount in range(0,amount+1,coins[0]):

			dp[0][currAmount] = 1

		for index in range(1,len(coins)):

			for currAmount in range(amount+1):

				pick = dp[index][currAmount-coins[index]] if currAmount >= coins[index] else 0
				notPick = dp[index-1][currAmount]

				dp[index][currAmount] = pick+notPick

		return dp[len(coins)-1][amount]
