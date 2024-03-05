class Solution:

	def firstMissingPositive(self,nums):

		nums.sort()

		result = 1

		for num in nums:

			if num > result:

				break

			if num == result:

				result += 1

		return result