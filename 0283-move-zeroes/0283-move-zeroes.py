class Solution:

	def moveZeroes(self, nums):

		slow = 0

		for fast in range(len(nums)):

			if nums[fast]:

				nums[slow] = nums[fast]

				slow += 1

		for remaining in range(slow, len(nums)):

			nums[remaining] = 0

  