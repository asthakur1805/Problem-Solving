class Solution:

	def candy(self,ratings):

		candies = [1]*len(ratings)

		for index in range(1,len(ratings)):

			if ratings[index] > ratings[index-1]:

				candies[index] = candies[index-1]+1

		totalCandies = candies[len(ratings)-1]

		for index in range(len(ratings)-2,-1,-1):

			if ratings[index] > ratings[index+1]:

				candies[index] = max(candies[index],candies[index+1]+1)
				
			totalCandies += candies[index]

		return totalCandies