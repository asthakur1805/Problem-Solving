class Solution:

	def rotate(self, nums, numRotations):

		copy = [0]*len(nums)

		for index, num in enumerate(nums):

			copy[(index+numRotations)%len(nums)] = num

		for index in range(len(nums)):

			nums[index] = copy[index]