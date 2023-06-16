class Solution:

	def calculate(self, inputStr):

		tempResult = 0
	
		operand = 0

		prevOperator = '+'

		result = 0

		for index, char in enumerate(inputStr):

			if self.isDigit(char):

				operand = operand * 10 + ord(char) - ord('0')

			if index == len(inputStr)-1 or char in ('+','-','*','/'):

				if prevOperator == '+':

					result += tempResult
					tempResult = operand

				elif prevOperator == '-':

					result += tempResult
					tempResult = -operand

				elif prevOperator == '*':

					tempResult *= operand

				else:

					tempResult = int(tempResult / operand)

				operand, prevOperator = 0, char

		result += tempResult

		return result

	def isDigit(self, char):

		return ord('0') <= ord(char) <= ord('9')