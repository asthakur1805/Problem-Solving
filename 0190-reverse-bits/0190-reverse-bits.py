class Solution:

	def reverseBits(self, number):

		result = 0

		for bitIndex in range(32):

			bit = (number >> bitIndex) & 1

			result = result | (bit << (31 - bitIndex))

		return result