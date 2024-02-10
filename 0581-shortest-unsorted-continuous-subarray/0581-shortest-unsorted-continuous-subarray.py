class Solution:

	def findUnsortedSubarray(self,nums):

		start, end = -1, -2

		currMax = float('-inf')

		for index in range(len(nums)):

			currMax = max(currMax,nums[index])

			if nums[index] < currMax:

				end = index

		currMin = float('inf')

		for index in range(len(nums)-1,-1,-1):

			currMin = min(currMin,nums[index])

			if nums[index] > currMin:

				start = index

		return end - start + 1