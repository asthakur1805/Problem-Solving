class Solution:

	def singleNumber(self, nums):

		xorResult = 0

		for num in nums:

			xorResult ^= num

		mask = xorResult & (-xorResult)

		result = [0, 0]

		for num in nums:

			if mask & num:

				result[0] ^= num

			else:

				result[1] ^= num

		return result