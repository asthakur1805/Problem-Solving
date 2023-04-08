class Solution:

	def hammingWeight(self, inputNumber):

		result = 0

		while inputNumber:

			inputNumber &= (inputNumber - 1)

			result += 1

		return result