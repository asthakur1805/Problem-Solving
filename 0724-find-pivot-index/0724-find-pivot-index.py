class Solution:

	def pivotIndex(self,nums):

		totalSum = 0

		for num in nums:

			totalSum += num

		leftSum = 0

		for candidateIndex in range(len(nums)):

			rightSum = totalSum - leftSum - nums[candidateIndex]

			if leftSum == rightSum:

				return candidateIndex

			leftSum += nums[candidateIndex]

		return -1

		
	