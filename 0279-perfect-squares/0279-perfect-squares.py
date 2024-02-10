class Solution:

	def numSquares(self,inputNumber):

		if self.isPerfectSquare(inputNumber):

			return 1

		firstSquareRoot = 1

		while firstSquareRoot*firstSquareRoot < inputNumber:

			secondSquare = inputNumber-firstSquareRoot*firstSquareRoot

			if self.isPerfectSquare(secondSquare):

				return 2

			firstSquareRoot += 1

		while inputNumber % 4 == 0:

			inputNumber //= 4

		if inputNumber % 8 == 7:

			return 4

		return 3

	def isPerfectSquare(self,inputNumber):

		squareRoot = int(inputNumber ** 0.5)

		return squareRoot * squareRoot == inputNumber