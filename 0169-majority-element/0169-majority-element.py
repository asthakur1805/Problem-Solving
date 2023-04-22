class Solution:

	def majorityElement(self, nums):

		maxCount, result = 0, None

		counts = {}

		for num in nums:

			counts[num] = counts.get(num, 0) + 1

			if counts[num] > maxCount:

				maxCount = counts[num]
				result = num

		return result