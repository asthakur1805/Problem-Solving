class Solution:

	def isValid(self, inputStr):

		stack = []

		closeToOpen = {
			')':'(', 
			'}':'{',
			']':'['
		}

		for char in inputStr:

			if char in closeToOpen:

				if stack and stack[-1] == closeToOpen[char]:

					stack.pop()

				else:

					return False

			else:

				stack.append(char)

		return not stack