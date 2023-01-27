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
	
	def sumOfSquares(self, num):

		result = 0

		while num:

			digit = num % 10

			result += digit ** 2

			num //= 10

		return result
			

	