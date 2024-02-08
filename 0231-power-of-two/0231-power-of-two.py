class Solution:

	def isPowerOfTwo(self,inputNumber):

		return inputNumber > 0 and (inputNumber & (inputNumber-1)) == 0

			