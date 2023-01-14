class Solution:

	def twoSum(self, nums, target):

		visitedNums = {}

		for index, value in enumerate(nums):

			diff = target - value

			if diff in visitedNums:

				return [visitedNums[diff], index]

			visitedNums[value] = index

		return []
			