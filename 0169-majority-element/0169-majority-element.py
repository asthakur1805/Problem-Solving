class Solution:

	def majorityElement(self, nums):

		count, result = 0, None

		for num in nums:

			if count == 0:

				result = num

			count += (1 if result == num else -1)

		return result