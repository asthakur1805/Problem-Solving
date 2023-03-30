class Solution:

	def flatten(self, root):

		self.prev = None

		self.helper(root)

	def helper(self, node):

		if not node:

			return

		self.helper(node.right)

		self.helper(node.left)

		node.right = self.prev
		node.left = None
		self.prev = node
