class Solution:

	def majorityElement(self, nums):

		maxCount, counts, result = 0, {}, None

		for num in nums:
	
			counts[num] = counts.get(num, 0) + 1

			result = num if counts[num] > maxCount else result

			maxCount = max(maxCount, counts[num])

		return result