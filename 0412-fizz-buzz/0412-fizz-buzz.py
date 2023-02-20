class Solution:

	def fizzBuzz(self, upperBound):

		fizzCount, buzzCount = 1, 1

		result = []

		for number in range(1, upperBound+1):

			if fizzCount == 3 and buzzCount == 5:

				result.append('FizzBuzz')
				fizzCount, buzzCount = 0, 0

			elif fizzCount == 3:

				result.append('Fizz')
				fizzCount = 0

			elif buzzCount == 5:

				result.append('Buzz')
				buzzCount = 0

			else:

				result.append(str(number))

			fizzCount, buzzCount = fizzCount + 1, buzzCount + 1

		return result
