class Solution:

	def deleteAndEarn(self,nums):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1
	
		nums = sorted(set(nums))

		dp = [0]*len(nums)

		dp[0] = nums[0] * counts[nums[0]]

		for index in range(1,len(nums)):

			currEarning = nums[index] * counts[nums[index]]

			deleteCurr = currEarning + (dp[index-1] if index > 0 and nums[index] != nums[index-1]+1 else dp[index-2])

			notDeleteCurr = dp[index-1]

			dp[index] = max(deleteCurr,notDeleteCurr)

		return dp[len(nums)-1]

				