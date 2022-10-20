class Solution:

	def majorityElement(self, nums):

		result, maxCount = None, 0

		counts = {}

		for num in nums:

			counts[num] = counts.get(num, 0) + 1

			if counts[num] > maxCount:

				result = num

				maxCount = counts[num]

		return result