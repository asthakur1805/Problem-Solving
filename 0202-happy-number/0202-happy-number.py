class Solution:

	def isHappy(self, inputNumber):

		visitedNums = set()

		while True:

			visitedNums.add(inputNumber)

			inputNumber = self.sumOfSquares(inputNumber)

			if inputNumber in visitedNums:

				break

		return inputNumber == 1

	def sumOfSquares(self, num):

		result = 0

		while num:

			digit = num % 10

			result += digit ** 2

			num //= 10

		return result