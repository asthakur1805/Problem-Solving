class Solution:

	def sortColors(self, nums):

		counts = {0:0, 1:0, 2:0}

		for num in nums:

			counts[num] += 1

		for index in range(counts[0]):

			nums[index] = 0

		for index in range(counts[0], counts[0]+counts[1]):

			nums[index] = 1

		for index in range(counts[0]+counts[1], counts[0]+counts[1]+counts[2]):

			nums[index] = 2