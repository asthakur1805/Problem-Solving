class Solution:

	def reverse(self, inputNumber):

		limit = 2 ** 31 - 1

		if inputNumber == -limit-1:
			return 0

		sign = 1 if inputNumber > 0 else -1

		inputNumber = abs(inputNumber)

		reversedNumber = 0

		while inputNumber:

			digit = inputNumber % 10

			if reversedNumber > (limit - digit) / 10:

				return 0

			reversedNumber = reversedNumber * 10 + digit

			inputNumber //= 10

		return reversedNumber * sign

		
		


		
		