class Solution:

	def longestConsecutive(self, nums):

		if not nums:

			return 0

		nums.sort()

		currLength, resultLength = 1, 0

		for index in range(1, len(nums)):

			if nums[index] != nums[index-1]:

				if nums[index] == nums[index-1] + 1:

					currLength += 1

				else:

					resultLength = max(currLength, resultLength)

					currLength = 1

		return max(resultLength, currLength)

