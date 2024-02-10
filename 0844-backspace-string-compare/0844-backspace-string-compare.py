class Solution:

	def backspaceCompare(self,firstStr,secondStr):

		firstStack, secondStack = self.helper(firstStr), self.helper(secondStr)

		if len(firstStack) != len(secondStack):

			return False

		while firstStack:

			if firstStack.pop() != secondStack.pop():

				return False

		return True

	def helper(self,inputStr):

		stack = []

		for char in inputStr:

			if char == '#':

				if stack:

					stack.pop()

			else:

				stack.append(char)

		return stack
			