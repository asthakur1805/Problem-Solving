class Solution:

	def countNodes(self,root):

		self.count = 0

		self.preorder(root)

		return self.count

	def preorder(self,node):

		if not node:

			return 0

		self.count += 1

		self.preorder(node.left)

		self.preorder(node.right)