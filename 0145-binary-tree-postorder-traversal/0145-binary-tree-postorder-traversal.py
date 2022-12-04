class Solution:

	def postorderTraversal(self, root):

		result = []

		self.helper(root, result)

		return result

	def helper(self, node, result):

		if not node:

			return

		self.helper(node.left, result)

		self.helper(node.right, result)

		result.append(node.val)