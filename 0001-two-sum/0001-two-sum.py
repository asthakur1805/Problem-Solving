class Solution:

	def twoSum(self, nums, target):

		visitedNums = {}

		for index, value in enumerate(nums):

			difference = target - value

			if difference in visitedNums:

				return [visitedNums[difference], index]

			visitedNums[value] = index

		return []