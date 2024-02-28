class Solution:

	def maxProfit(self,prices):

		return self.helper(prices,0,1,{})

	def helper(self,prices,index,canBuy,cache):

		if index >= len(prices):

			return 0

		if (index,canBuy) in cache:

			return cache[(index,canBuy)]

		if canBuy:

			buy = -prices[index]+self.helper(prices,index+1,0,cache)
			notBuy = self.helper(prices,index+1,1,cache)

			profit = max(buy,notBuy)

		else:

			sell = prices[index]+self.helper(prices,index+2,1,cache)
			notSell = self.helper(prices,index+1,0,cache)

			profit = max(sell,notSell)

		cache[(index,canBuy)] = profit
		return profit