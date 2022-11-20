class Solution:

	def moveZeroes(self, nums):

		slowPointer = 0

		for fastPointer in range(len(nums)):

			if nums[fastPointer]:

				nums[slowPointer], nums[fastPointer] = nums[fastPointer], nums[slowPointer]

				slowPointer += 1

		