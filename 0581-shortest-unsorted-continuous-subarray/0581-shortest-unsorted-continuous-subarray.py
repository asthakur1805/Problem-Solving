class Solution:

	def findUnsortedSubarray(self,nums):

		numsCopy = sorted(nums)

		firstMismatch = lastMismatch = -1

		firstIndex = 0

		for firstIndex in range(len(nums)):

			if nums[firstIndex] != numsCopy[firstIndex]:

				firstMismatch = lastMismatch = firstIndex
				break

		else:

			return 0

		for lastIndex in range(firstIndex+1,len(nums)):

			if nums[lastIndex] != numsCopy[lastIndex]:

				lastMismatch = lastIndex

		return lastMismatch - firstMismatch + 1

