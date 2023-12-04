class Solution:

	def fib(self,inputNumber):

		return self.memoization(inputNumber,{})

	def memoization(self,inputNumber,cache):

		if inputNumber <= 1: return inputNumber

		if inputNumber in cache: return cache[inputNumber]

		cache[inputNumber] = self.memoization(inputNumber-1,cache) + self.memoization(inputNumber-2,cache)

		return cache[inputNumber]