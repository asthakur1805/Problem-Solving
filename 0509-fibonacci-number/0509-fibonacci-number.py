class Solution:

	def fib(self,inputNumber):

		if inputNumber <= 1:

			return inputNumber

		first, second = 0, 1

		for _ in range(inputNumber-1):

			first, second = second, first+second

		return second

		