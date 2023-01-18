class Solution:

	def isHappy(self, number):

		visitedNums = set()

		while number not in visitedNums:

			if number == 1:

				return True

			visitedNums.add(number)

			number = self.sumOfSquares(number)

		return False

	def sumOfSquares(self, number):

		result = 0

		while number:

			digit = number % 10

			result += (digit ** 2)

			number //= 10

		return result