class Solution:

	def reverseBits(self, number):

		result = 0

		for index in range(32):

			bit = (number >> index) & 1

			result = result | bit

			result = result << 1

		return result >> 1