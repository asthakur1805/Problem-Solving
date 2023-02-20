class Solution:

	def isHappy(self, inputNumber):

		slow, fast = inputNumber, inputNumber

		while True:

			slow = self.sumOfSquares(slow)
			fast = self.sumOfSquares(self.sumOfSquares(fast))

			if slow == fast:

				break

		return slow == 1

	def sumOfSquares(self, inputNumber):

		result = 0

		while inputNumber:

			digit = inputNumber % 10

			result += digit ** 2

			inputNumber //= 10


		return result