class Solution:

	def findUnsortedSubarray(self,nums):

		start, end = -1, -2

		currMax, currMin = float('-inf'), float('inf')

		for index in range(len(nums)):

			currMax = max(currMax,nums[index])
			currMin = min(currMin,nums[len(nums)-1-index])

			if nums[index] < currMax:

				end = index

			if nums[len(nums)-1-index] > currMin:

				start = len(nums)-1-index

		return end - start + 1