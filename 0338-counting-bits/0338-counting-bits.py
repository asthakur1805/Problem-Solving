class Solution:

	def countBits(self,upperBound):

		return [self.countSetBits(num) for num in range(upperBound+1)]

	def countSetBits(self,inputNumber):

		result = 0

		while inputNumber:

			result += (inputNumber % 2)

			inputNumber //= 2

		return result

			