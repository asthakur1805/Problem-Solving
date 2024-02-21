class Solution:

	def canJump(self,nums):

		dp = [False] * len(nums)

		dp[len(nums)-1] = True

		for currIndex in range(len(nums)-2,-1,-1):

			for jumpSize in range(1,nums[currIndex]+1):

				if currIndex+jumpSize < len(nums) and dp[currIndex+jumpSize]:

					dp[currIndex] = True
					break

		return dp[0]
				