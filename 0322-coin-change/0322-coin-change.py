class Solution:

	def coinChange(self,coins,amount):

		prev = [float('inf')]*(amount+1)
		
		for currAmount in range(amount+1):

			prev[currAmount] = currAmount // coins[0] if currAmount % coins[0] == 0 else float('inf')

		for index in range(1,len(coins)):
		
			for currAmount in range(amount+1):

				pick = 1 + prev[currAmount-coins[index]] if currAmount >= coins[index] else float('inf')
				notPick = prev[currAmount]

				prev[currAmount] = min(pick,notPick)

		result = prev[amount]

		return -1 if result == float('inf') else result
