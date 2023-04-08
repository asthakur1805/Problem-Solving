class Solution:

	def majorityElement(self, nums):

		counts, result, maxCount = {}, None, 0

		for num in nums:

			counts[num] = counts.get(num, 0) + 1

		for num, count in counts.items():

			if count > maxCount:

				maxCount, result = count, num

		return result