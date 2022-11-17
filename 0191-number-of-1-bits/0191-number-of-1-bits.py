class Solution:

	def hammingWeight(self, num):

		result = 0

		for _ in range(32):

			result += (num & 1)
			num >>= 1

		return result
				