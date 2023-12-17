class Solution:

	def rob(self,nums):

		cache = [0]*len(nums)

		cache[0] = nums[0]

		for index in range(1,len(nums)):

			rob = nums[index] + cache[index-2] if index > 1 else nums[index]

			skip = cache[index-1]

			cache[index] = max(rob,skip)

		return cache[len(nums)-1]