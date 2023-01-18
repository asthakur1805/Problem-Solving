class Solution:

	def isHappy(self, number):

		slowPointer = number

		fastPointer = number

		while True:

			slowPointer = self.sumOfSquares(slowPointer)

			fastPointer = self.sumOfSquares(self.sumOfSquares(fastPointer))

			if slowPointer == fastPointer:

				break

		if slowPointer == 1:

			return True

		return False

	def sumOfSquares(self, number):

		result = 0

		while number:

			digit = number % 10

			result += (digit ** 2)

			number //= 10

		return result