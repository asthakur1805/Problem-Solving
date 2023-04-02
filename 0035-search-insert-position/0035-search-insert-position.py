class Solution:

	def searchInsert(self, nums, inputVal):

		for index, num in enumerate(nums):

			if inputVal <= num:

				return index

		return len(nums)