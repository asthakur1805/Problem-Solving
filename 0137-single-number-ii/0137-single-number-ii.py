class Solution:

	def singleNumber(self, nums):

		numCounts = {}

		for num in nums:

			numCounts[num] = numCounts.get(num, 0) + 1

		for num, count in numCounts.items():

			if count == 1:

				return num

		return