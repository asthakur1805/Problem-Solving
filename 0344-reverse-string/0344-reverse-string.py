class Solution:

	def reverseString(self, inputStr):

		stack = []

		for character in inputStr:

			stack.append(character)

		for index in range(len(inputStr)):

			inputStr[index] = stack.pop()

		