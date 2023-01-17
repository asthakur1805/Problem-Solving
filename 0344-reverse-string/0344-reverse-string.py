class Solution:

	def reverseString(self, inputStr):

		stack = []

		for index in range(len(inputStr)):

			stack.append(inputStr[index])

		for index in range(len(inputStr)):

			inputStr[index] = stack.pop()

