class Solution:

	def coinChange(self,coins,amount):

		def helper(index,currAmount,cache):

			if index == 0:

				return currAmount // coins[0] if currAmount % coins[0] == 0 else float('inf')

			if (index,currAmount) in cache:

				return cache[(index,currAmount)]

			pick = 1 + helper(index,currAmount-coins[index],cache) if currAmount >= coins[index] else float('inf')
			notPick = helper(index-1,currAmount,cache)

			cache[(index,currAmount)] = min(pick,notPick) 
			return min(pick,notPick)

		result = helper(len(coins)-1,amount,{})

		return result if result != float('inf') else -1

			



				