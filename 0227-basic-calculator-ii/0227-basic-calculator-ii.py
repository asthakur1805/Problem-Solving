class Solution:

	def calculate(self, inputStr):

		stack = []

		prevOperator = '+'

		secondOperand = 0

		for index, char in enumerate(inputStr):

			if self.isDigit(char):

				secondOperand = secondOperand * 10 + ord(char) - ord('0')

			if index == len(inputStr)-1 or (not self.isDigit(char) and char != ' '):

				if prevOperator == '+':

					stack.append(secondOperand)
	
				elif prevOperator == '-':

					stack.append(-secondOperand)

				elif prevOperator == '*':

					firstOperand = stack.pop()
	
					stack.append(firstOperand * secondOperand)

				elif prevOperator == '/':

					firstOperand = stack.pop()

					stack.append(int(firstOperand / secondOperand))

				secondOperand = 0
				prevOperator = char

		result = 0

		for num in stack:

			result += num

		return result

				

	def isDigit(self, char):

		return ord('0') <= ord(char) <= ord('9')