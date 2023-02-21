class Solution:

	def sumNumbers(self, root):

		return self.helper(root, 0)

	def helper(self, node, pathNumber):

		if not node:

			return 0

		if not node.left and not node.right:

			return pathNumber * 10 + node.val

		return self.helper(node.left, pathNumber * 10 + node.val) + self.helper(node.right, pathNumber * 10 + node.val)