class Solution:

	def evalRPN(self,tokens):

		stack = []

		for token in tokens:

			if token not in ("+","-","*","/"):

				currResult = int(token)

				
			else:

				secondOperand, firstOperand = stack.pop(), stack.pop()

				if token == "+":

					currResult = firstOperand + secondOperand

				elif token == "-":

					currResult = firstOperand - secondOperand

				elif token == "*":

					currResult = firstOperand * secondOperand

				else:

					currResult = int(firstOperand / secondOperand)

			stack.append(currResult)

		return stack.pop()	

	