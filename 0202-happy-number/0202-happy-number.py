class Solution:

	def isHappy(self, num):

		slowPointer, fastPointer = num, num

		while True:

			slowPointer = self.sumOfSquares(slowPointer)
			fastPointer = self.sumOfSquares(self.sumOfSquares(fastPointer))

			if slowPointer == fastPointer:

				break

		if slowPointer == 1:

			return True

		return False

	def sumOfSquares(self, num):

		result = 0

		while num:

			digit = num % 10

			result += digit ** 2

			num //= 10

		return result

		