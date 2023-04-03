class Solution:

	def mySqrt(self, square):

		if not square:

			return 0

		squareRoot = 1

		while True:

			if squareRoot <= square / squareRoot and square / (squareRoot + 1) < (squareRoot + 1):

				return squareRoot

			squareRoot += 1

		return