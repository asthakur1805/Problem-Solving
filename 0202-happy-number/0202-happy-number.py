class Solution:

	def isHappy(self, number):

		visitedNums = set()

		while True:

			if number == 1:

				return True

			if number in visitedNums:

				return False

			visitedNums.add(number)

			number = self.sumOfSquares(number)

		return

	def sumOfSquares(self, number):

		result = 0

		while number:

			digit = number % 10

			result += digit ** 2

			number //= 10

		return result