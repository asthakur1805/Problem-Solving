class Solution:

	def majorityElement(self, nums):

		result, count = None, 0

		for num in nums:

			result = num if count == 0 else result
			count += (1 if result == num else -1)

		return result
				