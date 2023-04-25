class Solution:

	def searchRange(self, nums, target):

		firstIndex, lastIndex = -1, -1

		for currIndex in range(len(nums)):

			if nums[currIndex] == target:

				firstIndex, lastIndex = currIndex, currIndex
				break

		else:

			return [firstIndex, lastIndex]

		for currIndex in range(firstIndex+1, len(nums)):

			if nums[currIndex] == target:

				lastIndex = currIndex

		return [firstIndex, lastIndex]
 
		