class Solution:

	def change(self,amount,coins):

		prev = [0]*(amount+1)

		for currAmount in range(0,amount+1,coins[0]):

			prev[currAmount] = 1

		for index in range(1,len(coins)):

			for currAmount in range(amount+1):

				pick = prev[currAmount-coins[index]] if currAmount >= coins[index] else 0
				notPick = prev[currAmount]

				prev[currAmount] = pick+notPick
	
		return prev[amount]
				

				
