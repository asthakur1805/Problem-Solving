class Solution:

	def maxProfit(self,k,prices):

		return self.helper(prices,0,1,k,{})

	def helper(self,prices,index,canBuy,maxTransactions,cache):

		if index == len(prices) or maxTransactions == 0:

			return 0

		if (index,canBuy,maxTransactions) in cache:
	
			return cache[(index,canBuy,maxTransactions)]

		if canBuy:

			buy = -prices[index]+self.helper(prices,index+1,0,maxTransactions,cache)
			notBuy = self.helper(prices,index+1,1,maxTransactions,cache)

			profit = max(buy,notBuy)

		else:

			sell = prices[index]+self.helper(prices,index+1,1,maxTransactions-1,cache)
			notSell = self.helper(prices,index+1,0,maxTransactions,cache)

			profit = max(sell,notSell)

		cache[(index,canBuy,maxTransactions)] = profit
		return profit

		
