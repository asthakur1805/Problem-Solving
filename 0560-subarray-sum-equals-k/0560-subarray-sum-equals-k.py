class Solution:

	def subarraySum(self, nums, K):

		result = 0

		countSubarraySum = {0:1}

		currSum = 0

		for num in nums:

			currSum += num

			if currSum - K in countSubarraySum:

				result += countSubarraySum[currSum-K]

			countSubarraySum[currSum] = countSubarraySum.get(currSum,0) + 1 

		return result