class Solution:

	def generateParenthesis(self, count):

		numLeftBrackets, numRightBrackets = count, count

		builder = ''

		result = []

		self.helper(builder, result, numLeftBrackets, numRightBrackets)

		return result


	def helper(self, builder, result, numLeftBrackets, numRightBrackets):

		if numLeftBrackets == 0 and numRightBrackets == 0:

			result.append(builder)

			return

		if numLeftBrackets > 0:

			self.helper(builder+'(', result, numLeftBrackets-1, numRightBrackets)

		if numRightBrackets > 0 and numLeftBrackets < numRightBrackets:

			self.helper(builder+')', result, numLeftBrackets, numRightBrackets-1)