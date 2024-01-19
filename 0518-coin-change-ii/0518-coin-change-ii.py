class Solution:

	def change(self,amount,coins):

		return self.helper(coins,len(coins)-1,amount,{})

	def helper(self,coins,index,amount,cache):

		if index == 0:

			return 1 if amount % coins[0] == 0 else 0

		if (index,amount) in cache:

			return cache[(index,amount)]

		pick = self.helper(coins,index,amount-coins[index],cache) if amount >= coins[index] else 0
		notPick = self.helper(coins,index-1,amount,cache)

		cache[(index,amount)] = pick + notPick
		return cache[(index,amount)]