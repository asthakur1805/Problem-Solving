class Solution:

	def fizzBuzz(self, upperLimit):

		result, fizz, buzz = [], 1, 1


		for num in range(1,upperLimit+1):

			if fizz == 3 and buzz == 5:

				result.append('FizzBuzz')

				fizz = 0
				buzz = 0

			elif fizz == 3:

				result.append('Fizz')

				fizz = 0

			elif buzz == 5:

				result.append('Buzz')

				buzz = 0

			else:

				result.append(str(num))

			fizz, buzz = fizz+1, buzz+1

		return result