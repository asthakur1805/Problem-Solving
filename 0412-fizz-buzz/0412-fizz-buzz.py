class Solution:

	def fizzBuzz(self, inputLimit):

		result = []

		for num in range(1, inputLimit+1):

			if not num % 3 and not num % 5:

				result.append("FizzBuzz")

			elif not num % 3:

				result.append("Fizz")

			elif not num % 5:

				result.append("Buzz")

			else:

				result.append(str(num))

		return result