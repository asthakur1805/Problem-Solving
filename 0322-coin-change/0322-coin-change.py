class Solution:

	def coinChange(self,coins,amount):

		result = self.helper(coins,len(coins)-1,amount,{})

		return -1 if result == float('inf') else result

	def helper(self,coins,index,amount,cache):

		if index == 0:

			return amount // coins[0] if amount % coins[0] == 0 else float('inf')

		if (index,amount) in cache:

			return cache[(index,amount)]

		pick = 1 + self.helper(coins,index,amount-coins[index],cache) if amount >= coins[index] else float('inf')
		notPick = self.helper(coins,index-1,amount,cache)

		cache[(index,amount)] = min(pick,notPick)
		return cache[(index,amount)]