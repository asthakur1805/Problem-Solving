class Solution:

	def fib(self,inputNumber):

		return self.bruteForce(inputNumber)

	def bruteForce(self,inputNumber):

		if inputNumber <= 1:

			return inputNumber

		return self.bruteForce(inputNumber-1) + self.bruteForce(inputNumber-2)