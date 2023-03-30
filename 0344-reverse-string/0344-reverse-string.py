class Solution:

	def reverseString(self, inputStr):

		stack = []

		for char in inputStr:

			stack.append(char)

		for index in range(len(inputStr)):

			inputStr[index] = stack.pop()

			

			