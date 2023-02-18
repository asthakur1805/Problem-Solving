class Solution:

	def hammingWeight(self, inputNumber):

		result = 0

		for bitPosition in range(32):

			if inputNumber & (1 << bitPosition):

				result += 1

		return result
		