class Solution:

	def candy(self,ratings):

		index, totalCandies = 1, len(ratings)

		while index < len(ratings):

			peak, dip = 0, 0

			if ratings[index] == ratings[index-1]:

				index += 1
				continue

			while index < len(ratings) and ratings[index] > ratings[index-1]:

				peak += 1
				totalCandies += peak
				index += 1

			while index < len(ratings) and ratings[index] < ratings[index-1]:

				dip += 1
				totalCandies += dip
				index += 1

			totalCandies -= min(peak,dip)

		return totalCandies
	