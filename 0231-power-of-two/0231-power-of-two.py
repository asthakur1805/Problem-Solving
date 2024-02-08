class Solution:

	def isPowerOfTwo(self,inputNumber):

		if inputNumber < 0:

			return False

		setBitCount = 0

		for bitPosition in range(32):

			setBitCount += (inputNumber & 1)
			inputNumber >>= 1

		return setBitCount == 1

			