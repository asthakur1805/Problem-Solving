class Solution:

	def findUnsortedSubarray(self,nums):

		numsIncreasing = sorted(nums)

		firstMismatch = lastMismatch = -1

		firstIndex = 0

		for firstIndex in range(len(nums)):

			if nums[firstIndex] != numsIncreasing[firstIndex]:

				firstMismatch = lastMismatch = firstIndex
				break
	
		else:

			return 0

		for lastIndex in range(firstIndex+1,len(nums)):

			if nums[lastIndex] != numsIncreasing[lastIndex]:

				lastMismatch = lastIndex

		return lastMismatch-firstMismatch+1