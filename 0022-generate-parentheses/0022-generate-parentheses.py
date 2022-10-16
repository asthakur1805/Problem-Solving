class Solution:

	def generateParenthesis(self, numParentheses):

		numLeft = numRight = numParentheses

		currentStr = []

		result = []

		self.helper(numLeft, numRight, currentStr, result)

		return result

	def helper(self, numLeft, numRight, currentStr, result):

		if numLeft == 0 and numRight == 0:

			result.append(''.join(currentStr.copy()))

			return

		if numLeft > 0:

			currentStr.append('(')
			self.helper(numLeft-1, numRight, currentStr, result)
			currentStr.pop()

		if numLeft < numRight:

			currentStr.append(')')
			self.helper(numLeft, numRight-1, currentStr, result)
			currentStr.pop()
		