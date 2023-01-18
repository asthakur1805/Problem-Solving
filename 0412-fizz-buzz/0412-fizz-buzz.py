class Solution:

	def fizzBuzz(self, inputEnd):

		result = []

		for num in range(1, inputEnd+1):
		
			isFizz = 'Fizz' if not num % 3 else ''

			isBuzz = 'Buzz' if not num % 5 else ''

			result.append(str(num) if not isFizz and not isBuzz else f'{isFizz}{isBuzz}')

		return result
			