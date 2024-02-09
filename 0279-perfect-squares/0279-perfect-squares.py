class Solution:

	def numSquares(self,inputNumber):

		return self.helper(inputNumber,{})

	def helper(self,inputNumber,cache):

		if inputNumber == 0:

			return 0

		if inputNumber in cache:

			return cache[inputNumber]

		currNumber, result = 1, inputNumber

		while currNumber * currNumber <= inputNumber:

			result = min(result,1+self.helper(inputNumber-currNumber*currNumber,cache))

			currNumber += 1

		cache[inputNumber] = result
		return result

