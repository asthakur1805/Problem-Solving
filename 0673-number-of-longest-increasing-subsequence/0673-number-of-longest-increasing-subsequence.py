class Solution:

	def findNumberOfLIS(self,nums):

		dp = [1]*len(nums)
		counts = [1]*len(nums)

		resultLength = 1

		for currIndex in range(1,len(nums)):

			for prevIndex in range(currIndex):

				if nums[currIndex] > nums[prevIndex]:

					if dp[prevIndex] + 1 > dp[currIndex]:

						dp[currIndex] = dp[prevIndex] + 1
						counts[currIndex] = counts[prevIndex]

					elif dp[prevIndex] + 1 == dp[currIndex]:

						counts[currIndex] += counts[prevIndex]

			resultLength = max(resultLength,dp[currIndex])

		resultCount = 0

		for currIndex, currLength in enumerate(dp):

			if currLength == resultLength:

				resultCount += counts[currIndex]

		return resultCount