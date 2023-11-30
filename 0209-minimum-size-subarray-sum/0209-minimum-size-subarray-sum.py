class Solution:

	def minSubArrayLen(self,target,nums):

		start, currSum, result = 0, 0, float('inf')

		for end in range(len(nums)):

			currSum += nums[end]

			while currSum >= target:

				result = min(result,end-start+1)

				currSum -= nums[start]

				start += 1

		return 0 if result == float('inf') else result
 
		