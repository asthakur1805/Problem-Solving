class Solution:

	def preorderTraversal(self, root):

		result = []

		self.helper(root, result)

		return result

	def helper(self, node, result):

		if not node:

			return

		result.append(node.val)

		self.helper(node.left, result)

		self.helper(node.right, result)