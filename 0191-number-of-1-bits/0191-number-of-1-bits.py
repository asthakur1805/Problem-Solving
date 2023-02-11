class Solution:

	def hammingWeight(self, number):

		result = 0

		for bitPosition in range(32):

			if (number >> bitPosition) & 1:

				result += 1

		return result