class Solution:

	def sumNumbers(self, root):

		self.resultSum = 0

		self.helper(root, 0)

		return self.resultSum

	def helper(self, node, pathNumber):

		if not node:
		
			return

		pathNumber = pathNumber * 10 + node.val

		if not node.left and not node.right:

			self.resultSum += pathNumber

		self.helper(node.left, pathNumber)

		self.helper(node.right, pathNumber)