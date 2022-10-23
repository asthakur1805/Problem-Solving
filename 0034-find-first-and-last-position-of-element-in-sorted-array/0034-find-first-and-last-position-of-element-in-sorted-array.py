class Solution:

	def searchRange(self, nums, target):

		numsLength = len(nums)

		for index in range(numsLength):

			if nums[index] == target:
				
				lastIndex = firstIndex = index
				break

		else:

			return [-1, -1]

		for index in range(firstIndex+1,numsLength):

			if nums[index] != target:

				break

			lastIndex = index

		return [firstIndex, lastIndex]

		 