class Solution:

	def removeDuplicates(self, nums):

		if len(nums) < 1:

			return 

		slowPointer = 1

		for fastPointer in range(1, len(nums)):

			if nums[slowPointer-1] != nums[fastPointer]:

				nums[slowPointer] = nums[fastPointer]
				slowPointer += 1

		return slowPointer