class Solution:

	def deleteAndEarn(self,nums):

		counts = {}

		for num in nums:

			counts[num] = counts.get(num,0) + 1
	
		nums = sorted(set(nums))

		dp = [0]*len(nums)

		firstPrev = nums[0] * counts[nums[0]]

		secondPrev = 0

		for index in range(1,len(nums)):

			currEarning = nums[index] * counts[nums[index]]

			deleteCurr = currEarning + (firstPrev if index > 0 and nums[index] != nums[index-1]+1 else secondPrev)

			notDeleteCurr = firstPrev


			secondPrev, firstPrev = firstPrev, max(deleteCurr,notDeleteCurr)

		return firstPrev

				