class Solution:

	def getSum(self, firstNumber, secondNumber):

		mask, INT_MAX = 0xFFFFFFFF, 0x7FFFFFFF

		while secondNumber:

			carry = (firstNumber & secondNumber) << 1
			firstNumber = (firstNumber ^ secondNumber) & mask
			secondNumber = carry & mask

		return firstNumber if firstNumber <= INT_MAX else firstNumber | (~mask)