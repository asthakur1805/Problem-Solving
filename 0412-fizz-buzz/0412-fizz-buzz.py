class Solution:

	def fizzBuzz(self, upperBound):

		result = []

		for num in range(1, upperBound+1):

			if num % 15 == 0:

				result.append('FizzBuzz')

			elif num % 3 == 0:

				result.append('Fizz')

			elif num % 5 == 0:

				result.append('Buzz')

			else:

				result.append(str(num))

		return result