class Solution:

	def postorder(self, root):

		result = []

		self.helper(root, result)

		return result

	def helper(self, node, result):

		if not node:

			return

		for childNode in node.children:

			self.helper(childNode, result)

		result.append(node.val)