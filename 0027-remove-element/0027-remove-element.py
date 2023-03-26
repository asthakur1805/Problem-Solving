class Solution:

	def removeElement(self, nums, val):

		slowPointer = 0

		for fastPointer in range(len(nums)):

			if nums[fastPointer] != val:

				nums[slowPointer], nums[fastPointer] = nums[fastPointer], nums[slowPointer]

				slowPointer += 1

		return slowPointer