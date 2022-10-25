class Solution:

	def sortColors(self, nums):

		numCounts = {key:0 for key in [0,1,2]}

		for num in nums:

			numCounts[num] += 1

		index = 0

		for _ in range(numCounts[0]):

			nums[index] = 0

			index += 1

		for _ in range(numCounts[1]):

			nums[index] = 1

			index += 1

		for _ in range(numCounts[2]):

			nums[index] = 2

			index += 1


		