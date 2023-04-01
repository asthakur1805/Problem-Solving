class Solution:

	def fizzBuzz(self, inputLimit):

		fizz, buzz, result = 1, 1, []

		for num in range(1, inputLimit+1):

			if fizz == 3 and buzz == 5:

				result.append("FizzBuzz")
				fizz, buzz = 0, 0

			elif fizz == 3:

				result.append("Fizz")
				fizz = 0

			elif buzz == 5:

				result.append("Buzz")
				buzz = 0
	
			else:

				result.append(str(num))

			fizz += 1
			buzz += 1

		return result