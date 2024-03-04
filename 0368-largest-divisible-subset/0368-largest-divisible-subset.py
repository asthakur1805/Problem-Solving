class Solution:

	def largestDivisibleSubset(self,nums):

		nums.sort()

		dp = [1]*len(nums)

		trace = [-1]*len(nums)

		for currIndex in range(1,len(nums)):

			for prevIndex in range(currIndex):

				if nums[currIndex] %  nums[prevIndex] == 0 and 1 + dp[prevIndex] >= dp[currIndex]:

						dp[currIndex] = 1 + dp[prevIndex]
						trace[currIndex] = prevIndex
						
		resultIndex, resultLength = 0, 0

		for currIndex,currLength in enumerate(dp):

			if currLength > resultLength:

				resultLength, resultIndex = currLength, currIndex

		result = []

		while True:

			result.append(nums[resultIndex])

			if len(result) == resultLength:

				result.reverse()
				return result

			resultIndex = trace[resultIndex]
				

		
				

				

					