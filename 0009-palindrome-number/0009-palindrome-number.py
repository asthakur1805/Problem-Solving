class Solution:

	def isPalindrome(self, inputNumber):

		if inputNumber < 0 or inputNumber and not inputNumber % 10:

			return False

		reversedNumber = 0

		while reversedNumber < inputNumber:

			digit = inputNumber % 10

			reversedNumber = reversedNumber * 10 + digit

			inputNumber //= 10

		return reversedNumber == inputNumber or reversedNumber // 10 == inputNumber