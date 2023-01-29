class Solution:

	def rotate(self, nums, numRotations):

		clone = nums.copy()

		for index in range(len(nums)):

			clone[(index+numRotations)%len(nums)] = nums[index]

		for index in range(len(nums)):

			nums[index] = clone[index]