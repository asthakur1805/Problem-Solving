class Solution:

	def preorder(self, root):

		result = []

		self.helper(root, result)

		return result

	def helper(self, node, result):

		if not node:

			return

		result.append(node.val)

		for childNode in node.children:

			self.helper(childNode, result)