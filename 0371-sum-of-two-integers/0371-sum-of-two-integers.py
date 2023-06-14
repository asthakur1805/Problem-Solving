class Solution:

	def getSum(self, firstNumber, secondNumber):

		maxPositiveLimit, mask = 0x7FFFFFFF, 0xFFFFFFFF

		while secondNumber:

			carry = (firstNumber & secondNumber) << 1

			firstNumber = (firstNumber ^ secondNumber) & mask

			secondNumber = carry & mask

		return firstNumber if firstNumber <= maxPositiveLimit else (firstNumber | ~mask)