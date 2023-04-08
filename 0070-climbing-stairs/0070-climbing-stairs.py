class Solution:

	def climbStairs(self, inputNumber):

		first, second = 1, 1

		for _ in range(inputNumber-1):

			temp = second
			
			second += first

			first = temp

		return second

			