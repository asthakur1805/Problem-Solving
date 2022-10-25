class Solution:

	def removeDuplicates(self, nums):

		if len(nums) < 2:

			return len(nums)


		slowPointer = 2

		for fastPointer in range(2, len(nums)):

			if nums[slowPointer-2] != nums[fastPointer]:

				nums[slowPointer] = nums[fastPointer]
				slowPointer += 1


		return slowPointer

		