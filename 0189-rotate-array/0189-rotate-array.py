class Solution:

	def rotate(self, nums, rotations):

		numsLength = len(nums)

		rotated = [0] * numsLength 

		for index in range(len(nums)):

			rotated[(index+rotations) % numsLength] = nums[index]

		for index in range(len(nums)):

			nums[index] = rotated[index]

