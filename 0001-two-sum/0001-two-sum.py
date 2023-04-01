class Solution:

	def twoSum(self, nums, target):

		numsLength = len(nums)

		for firstIndex in range(numsLength-1):

			for secondIndex in range(firstIndex+1, numsLength):

				if nums[firstIndex] + nums[secondIndex] == target:

					return [firstIndex, secondIndex]

		return []