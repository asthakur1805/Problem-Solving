class Solution:

	def sumNumbers(self, root):

		self.resultSum = 0

		self.helper(root, 0)

		return self.resultSum

	def helper(self, node, currSum):

		if not node:

			return

		currSum = currSum * 10 + node.val

		if not node.left and not node.right:

			self.resultSum += currSum

		self.helper(node.left, currSum)

		self.helper(node.right, currSum)