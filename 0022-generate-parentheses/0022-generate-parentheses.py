class Solution:

	def generateParenthesis(self, numParenthesis):

		leftCount = rightCount = numParenthesis

		currStr, result = [], []

		self.helper(leftCount, rightCount, currStr, result)

		return result

	def helper(self, leftCount, rightCount, currStr, result):

		if leftCount == 0 and rightCount == 0:

			result.append(''.join(currStr.copy()))

			return

		if leftCount > 0:

			currStr.append('(')
			self.helper(leftCount-1, rightCount, currStr, result)
			currStr.pop()

		if rightCount > leftCount:

			currStr.append(')')
			self.helper(leftCount, rightCount-1, currStr, result)
			currStr.pop()

		
	