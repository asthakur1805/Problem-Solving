class Solution:

	def hammingWeight(self, inputNumber):

		result = 0

		while inputNumber:

			result += (inputNumber & 1)

			inputNumber >>= 1

		return result