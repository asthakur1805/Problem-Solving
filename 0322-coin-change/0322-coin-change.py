class Solution:

	def coinChange(self,coins,amount):

		dp = [[float('inf')]*(amount+1) for _ in range(len(coins))]

		for currAmount in range(amount+1):

			dp[0][currAmount] = currAmount // coins[0] if currAmount % coins[0] == 0 else float('inf')

		for index in range(1,len(coins)):

			for currAmount in range(amount+1):

				pick = 1 + dp[index][currAmount-coins[index]] if currAmount >= coins[index] else float('inf')
				notPick = dp[index-1][currAmount]

				dp[index][currAmount] = min(pick,notPick)

		result = dp[len(coins)-1][amount]

		return -1 if result == float('inf') else result
